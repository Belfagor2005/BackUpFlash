#!/usr/bin/python
# -*- coding: utf-8 -*-

# RAED & mfaraj57 (c) 2018
# Code RAED & mfaraj57

from .tools.skin import SKIN_full_main
from .tools.Console import Console
from .tools.bftools import (logdata, dellog, getboxtype, getmDevices, trace_error, getversioninfo, getimage_name)
from .tools.compat import PY3
from .tools.backup import doBackUpInternal, doBackUpExternal

from Components.ActionMap import ActionMap
from Components.config import getConfigListEntry, ConfigSubsection, config, ConfigYesNo, ConfigSelection, configfile, ConfigText
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from enigma import eTimer, quitMainloop
from os import listdir as os_listdir
from Plugins.Plugin import PluginDescriptor
from Screens.ChoiceBox import ChoiceBox
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Screens.VirtualKeyBoard import VirtualKeyBoard
from Tools.Directories import resolveFilename, fileExists, SCOPE_MEDIA
import datetime
import os


BRANDOS = '/var/lib/dpkg/status'  # DreamOS
BAINIT = '/sbin/bainit'
BAINFO = '/.bainfo'

boxtype = getboxtype()

Ver = getversioninfo()

config.backupflashe = ConfigSubsection()
config.backupflashe.update = ConfigYesNo(default=True)
config.backupflashe.shutdown = ConfigYesNo(default=False)
config.backupflashe.cleanba = ConfigYesNo(default=False)
config.backupflashe.flashAllow = ConfigYesNo(default=False)
config.backupflashe.path_left = ConfigText(default=resolveFilename(SCOPE_MEDIA))

image_formats = [('xz', 'xz'), ('gz', 'gz')]
config.backupflashe.image_format = ConfigSelection(default="xz", choices=image_formats)
xz_options = []
if boxtype == "dm520":
    xz_options.append(("1", "1"))
    xz_options.append(("2", "2"))
    xz_options.append(("3", "3"))
    xz_options.append(("4", "4"))
else:
    xz_options.append(("1", "1"))
    xz_options.append(("2", "2"))
    xz_options.append(("3", "3"))
    xz_options.append(("4", "4"))
    xz_options.append(("5", "5"))
    xz_options.append(("6", "6"))
config.backupflashe.xzcompression = ConfigSelection(default="1", choices=xz_options)
config.backupflashe.gzcompression = ConfigSelection(default="3", choices=xz_options)

k = open("/proc/cmdline", "r")
cmd = k.read()
k.close()

mounted_devices = getmDevices()
getname = getimage_name()
now = datetime.datetime.now()
DATETIME = now.strftime('%Y-%m-%d-%H-%M')

if boxtype == "dm520":
    if cmd.find("root=/dev/sda1") != -1:
        rootfs = "root=/dev/sda1"
    else:
        rootfs = "root=ubi0:dreambox-rootfs"
else:
    rootfs = "root=/dev/mmcblk0"


# Path of images on External Flash checking
searchPaths = []


def initPaths():
    if fileExists("/proc/mounts"):
        for line in open("/proc/mounts"):
            if "/dev/sd" in line or "/dev/disk/by-uuid/" in line or "/dev/mmc" in line:
                Path = line.split()[1].replace("\\040", " ").split(",")
                for dirName in Path:
                    if os.path.isdir(dirName + "/open-multiboot"):
                        return searchPaths.append(dirName + "/open-multiboot")
                    elif os.path.isdir(dirName + "/ImageBoot"):
                        return searchPaths.append(dirName + "/ImageBoot")
    return


initPaths()
CHECKBOOT = ''.join(searchPaths).split("/")[-1]

if os.path.isdir("/media/ba/ba"):
    IMAGLISTEPATH = "/media/ba/ba"  # Directory of BarryAllen images
    ExternalImages = True
    TEXT_CHOOSE = _("Images from BarryAllen")
elif os.path.isdir("/media/at"):
    IMAGLISTEPATH = "/media/at"  # Directory of AlanTuring images
    ExternalImages = True
    TEXT_CHOOSE = _("Images from AlanTuring")
elif os.path.isdir("/media/egamiboot/EgamiBootI"):
    IMAGLISTEPATH = "/media/egamiboot/EgamiBootI"  # Directory of Egami images
    ExternalImages = True
    TEXT_CHOOSE = _("Images from EgamiBoot")
else:
    IMAGLISTEPATH = next((p for p in searchPaths if os.path.isdir(p)), "")
    ExternalImages = bool(IMAGLISTEPATH)
    
    if ExternalImages:
        if CHECKBOOT == "open-multiboot":
            NAMEBOOT = "OpenMultiboot"
        elif CHECKBOOT == "ImageBoot":
            NAMEBOOT = "NeoBoot"
        else:
            NAMEBOOT = "Unknown"
        TEXT_CHOOSE = _("Images from %s" % NAMEBOOT)
    else:
        TEXT_CHOOSE = ""

####


class full_main(Screen, ConfigListScreen):

    def __init__(self, session):
        global rootfs
        Screen.__init__(self, session)
        self.list = []
        ConfigListScreen.__init__(self, self.list, on_change=self.changedEntry)
        self.onChangedEntry = []
        self.skin = SKIN_full_main
        self["key_green"] = Label(_("Flash Image"))
        self["key_yellow"] = Label(_("Flash online"))
        self["key_blue"] = Label(_("Backup Image"))
        self["key_red"] = Label(_("Recovery Mode"))
        self["lab1"] = Label("Detecting mounted devices")
        self["key_green"].hide()
        self["key_blue"].hide()
        self["key_yellow"].hide()
        self["help"] = StaticText()
        self["actions"] = ActionMap(
            [
                "WizardActions",
                "ColorActions",
                "MenuActions"
            ],
            {
                "green": self.doFlash,
                "blue": self.BackUpListSelect,
                "yellow": self.flashOnline,
                "menu": self.showMenuoptions,
                "red": self.red,
                "back": self.close
            }
        )
        self.deviceok = True
        self.new_version = Ver
        self.timer = eTimer()
        try:
            self.timer.callback.append(self.updateList)
        except:
            self.timer_conn = self.timer.timeout.connect(self.updateList)
        self.timer.start(6, 1)
        self.onLayoutFinish.append(self.layoutFinished)

    def layoutFinished(self):
        if config.backupflashe.update.value:
            self.checkupdates()
        self.setTitle("Backup And Flash by RAED & mfaraj57 - V " + Ver)
        self["config"].onSelectionChanged.append(self.updateHelp)

    def updateList(self):
        dellog()
        self.checkupdates()
        if len(mounted_devices) > 0:
            self.deviceok = True
            self["lab1"].setText(_("Do Flash New Image or Full Backup Image."))
            self["key_green"].show()
            self["key_blue"].show()
            self["key_yellow"].show()
            config.backupflashe.device_path = ConfigSelection(choices=mounted_devices)
            self.createSetup()
        else:
            self["lab1"].setText(_("Sorry no device mounted found.\nPlease check your media in devices manager."))
            self["key_green"].hide()
            self["key_blue"].hide()
            self["key_yellow"].hide()
            self.deviceok = False

    def createSetup(self):
        self.list = []
        self.list.append(getConfigListEntry(('Path to store Full Backup'), config.backupflashe.device_path, _("This option to set the path of Backup/Flash directory")))
        self.list.append(getConfigListEntry(('Select Format to Compress BackUp'), config.backupflashe.image_format, _("This option to select the type of compress option")))
        if config.backupflashe.image_format.value == "xz":
            self.list.append(getConfigListEntry(("xz") + " " + _("Compression") + " " + _("(1-6)"), config.backupflashe.xzcompression, _("This option to set stringe value of Compress image (The higher the value, the longer the operation time, but the smaller the backup size)")))
        elif config.backupflashe.image_format.value == "gz":
            self.list.append(getConfigListEntry(("gz") + " " + _("Compression") + " " + _("(1-6)"), config.backupflashe.gzcompression, _("This option to set stringe value of Compress image (The higher the value, the longer the operation time, but the smaller the backup size)")))
        else:
            pass
        self.list.append(getConfigListEntry(('Enable shutdown box after backup'), config.backupflashe.shutdown, _("This option to Enable or Disable Shutdown Box After Finished Backup")))
        self.list.append(getConfigListEntry(('Clean image from BA symlink before backup'), config.backupflashe.cleanba, _("This option for remove BarryAllen symlink from image Before Start Backup")))
        self['config'].list = self.list
        self['config'].l.setList(self.list)

    def updateHelp(self):
        cur = self["config"].getCurrent()
        if cur:
            self["help"].text = cur[2]

    def changedEntry(self):
        self.createSetup()
        self.configsSave()

    def doFlash(self):
        self.session.open(MessageBox, "Sorry Flash feature not working.\nPlease Flash the image from recovery mode more safe more stable.", MessageBox.TYPE_ERROR, timeout=8)

    def BackUpListSelect(self):
        list = []
        list.append(("Backup Current Image", "Do Backup From Current Flash image"))
        if ExternalImages is True:
            list.append(("Backup External Image", "Do Backup From External Flash image"))
        self.session.openWithCallback(self.BackUpSelect, ChoiceBox, _('Select Backup Option'), list)

    def BackUpSelect(self, select):
        if select:
            if select[0] == "Backup External Image":  # BackUp External Flash
                self.session.openWithCallback(self.askForTarget, ChoiceBox, _("%s") % TEXT_CHOOSE, self.imagelistbackup())
            else:  # BackUp Internal Flash
                self.nameBackUp()
        else:
            self.close()

# BackUp Internal Flash
    def nameBackUp(self):
        imagename = '%s-%s-%s' % (getname, boxtype, DATETIME)
        self.session.openWithCallback(self.doBackUpInt, VirtualKeyBoard, title=_("Please Enter Name For Backup Image"), text="%s" % imagename)

    def doBackUpInt(self, target):
        if target is None:
            return
        else:
            self.configsSave()
            if self.deviceok:
                try:
                    image_name = target
                    device_path = self['config'].list[0][1].getText()
                    image_formats = self['config'].list[1][1].getText()
                    image_compression_value = self['config'].list[2][1].getText()
                    self.session.open(doBackUpInternal, image_name, device_path, image_formats, image_compression_value)
                except:
                    trace_error()
                    pass

# BackUp External Flash
    def imagelistbackup(self):
        imageslist = []
        for line in os_listdir(IMAGLISTEPATH):
            if line.startswith("."):
                continue
            imageslist.append((line, line))
        imageslist.sort()
        return imageslist

    def askForTarget(self, source):
        if source is None:
            return
        else:
            self.configsSave()
            self.getname = source[1].rstrip()
            self.image_path = IMAGLISTEPATH + "/" + self.getname
            self.imagename = '%s-%s-%s' % (self.getname, boxtype, DATETIME)
            self.device_path = self['config'].list[0][1].getText()
            self.image_formats = self['config'].list[1][1].getText()
            self.image_compression_value = self['config'].list[2][1].getText()
            self.session.openWithCallback(self.doBackUpExt, VirtualKeyBoard, title=_("Please Enter Name For Backup Image"), text="%s" % self.imagename)

    def doBackUpExt(self, target):
        if target is None:
            return
        else:
            if self.deviceok:
                try:
                    image_name = target
                    image_path = self.image_path
                    device_path = self.device_path
                    image_formats = self.image_formats
                    image_compression_value = self.image_compression_value
                    self.session.open(doBackUpExternal, image_name, image_path, device_path, image_formats, image_compression_value)
                except:
                    trace_error()
                    pass
#

    def red(self,):
        self.session.openWithCallback(self.GoRecovery, MessageBox, _('Really shutdown now (To Go to Recovery Mode) ?!!'), MessageBox.TYPE_YESNO)

    def GoRecovery(self, answer=False):
        if answer:
            try:
                with open("/proc/stb/fp/boot_mode", "w") as b:
                    b.write("rescue")
                quitMainloop(2)
            except (IOError, OSError) as e:
                print("Error access /proc/stb/fp/boot_mode:", e)

    def flashOnline(self,):
        configfile.save()
        from .tools.flashonline import teamsScreen
        device_path = self['config'].list[0][1].getText()
        # logdata('selected device path', device_path)
        self.session.open(teamsScreen, device_path)

    def configsSave(self):
        for x in self['config'].list:
            x[1].save()
        configfile.save()

    def showMenuoptions(self):
        choices = []
        self.list = []
        EnablecheckUpdate = config.backupflashe.update.value
        choices.append(("Install backupflash version %s" % self.new_version, "Install"))
        if EnablecheckUpdate is False:
            choices.append(("Press Ok to [Enable checking for Online Update]", "enablecheckUpdate"))
        else:
            choices.append(("Press Ok to [Disable checking for Online Update]", "disablecheckUpdate"))
        self.session.openWithCallback(self.choicesback, ChoiceBox, _('select task'), choices)

    def choicesback(self, select):
        if select:
            if select[1] == "Install":
                self.install(True)
            elif select[1] == "enablecheckUpdate":
                config.backupflashe.update.value = True
                config.backupflashe.update.save()
                configfile.save()
            elif select[1] == "disablecheckUpdate":
                config.backupflashe.update.value = False
                config.backupflashe.update.save()
                configfile.save()

    def checkupdates(self):
        try:
            from twisted.web.client import getPage, error
            url = b'https://raw.githubusercontent.com/fairbird/BackUpFlash/main/installer.sh'
            getPage(url, timeout=10).addCallback(self.parseData).addErrback(self.errBack)
        except Exception as error:
            trace_error()
            print(error)

    def errBack(self, error=None):
        logdata("errBack-error", error)

    def parseData(self, data):
        if PY3:
            data = data.decode("utf-8")
        else:
            data = data.encode("utf-8")
        if data:
            lines = data.split("\n")
            for line in lines:
                # line=str(line)
                if line.startswith("version"):
                    self.new_version = line.split("=")[1]
                    # break #if enabled the for loop will exit before reading description line
                if line.startswith("description"):
                    self.new_description = line.split("=")[1]
                    break
        if float(Ver) >= float(self.new_version):
            logdata("Updates", "No new version available")
        else:
            new_version = self.new_version
            new_description = self.new_description
            self.session.openWithCallback(self.install, MessageBox, _('New version %s is available.\n\n%s.\n\nDo want ot install now.' % (new_version, new_description)), MessageBox.TYPE_YESNO)

    def install(self, answer=False):
        try:
            if answer:
                cmdlist = []
                cmd = 'wget https://raw.githubusercontent.com/fairbird/BackUpFlash/main/installer.sh -O - | /bin/sh'
                cmdlist.append(cmd)
                self.session.open(Console, title='Installing last update, enigma will be started after install', cmdlist=cmdlist, finishedCallback=self.myCallback, closeOnSuccess=False)
        except:
            trace_error()

    def myCallback(self, result):
        return


def main(session, **kwargs):
# mounted_devices = getmDevices()
# if len(mounted_devices) > 0:
    session.open(full_main)
# else:
#   session.open(MessageBox, "Sorry no device mounted found.\nPlease check your media in devices manager.", MessageBox.TYPE_ERROR,timeout=8)


def Plugins(**kwargs):
    result = [PluginDescriptor(
              name=_("BackupFlash"),
              description=_("Backup And Flash Images"),
              where=PluginDescriptor.WHERE_PLUGINMENU,
              icon='plugin.png',
              fnc=main,
              ),]
    return result
