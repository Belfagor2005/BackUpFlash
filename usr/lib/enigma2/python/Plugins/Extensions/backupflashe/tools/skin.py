# RAED & mfaraj57 &  (c) 2018
# Code RAED & mfaraj57
# Update 17-11-2018 Add download images option

from enigma import getDesktop
import os
from .bftools import getversioninfo

Ver, lastbuild, enigmaos = getversioninfo()
sz_w = getDesktop(0).size().width()


def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS


if sz_w == 2560:
    if DreamOS():
        SKIN_full_main = """
            <screen position="center,center" size="1528,800" title="Flash And Full Backup" backgroundColor="#16000000" flags="wfNoBorder">
                <widget source="Title" render="Label" font="Regular;47" foregroundColor="#00bab329" position="38,7" size="1447,60" transparent="1" />
                <widget name="config" position="38,74" size="1447,374" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000" zPosition="1" />
                <widget source="help" render="Label" position="38,460" size="1443,174" font="Regular;38" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" transparent="1" zPosition="1" />
                <widget name="lab1" position="38,642" size="1447,84" font="Regular;40" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" zPosition="1" />
                <widget name="key_red" position="40,727" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_green" position="406,727" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_yellow" position="771,727" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_blue" position="1136,727" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <eLabel position="40,777" size="350,8" backgroundColor="#00ff0000" zPosition="4" />
                <eLabel position="406,777" size="350,8" backgroundColor="#0000ff00" zPosition="4" />
                <eLabel position="771,777" size="350,8" backgroundColor="#00ffff00" zPosition="4" />
                <eLabel position="1137,777" size="350,8" backgroundColor="#000000ff" zPosition="4" />
            </screen>"""
    else:
        SKIN_full_main = """
            <screen position="center,center" size="1528,800" title="Flash And Full Backup" backgroundColor="#16000000" flags="wfNoBorder">
                <widget source="Title" render="Label" font="Regular;47" foregroundColor="#00bab329" position="38,7" size="1447,60" transparent="1"/>
                <widget name="config" font="Regular;40" itemHeight="54" position="38,74" size="1447,374" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000" zPosition="1"/>
                <widget source="help" render="Label" position="38,460" size="1443,174" font="Regular;38" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" transparent="1" zPosition="1"/>
                <widget name="lab1" position="38,642" size="1447,84" font="Regular;40" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" zPosition="1" />
                <widget name="key_red" position="40,727" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_green" position="406,727" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_yellow" position="771,727" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_blue" position="1136,727" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <eLabel position="40,777" size="350,8" backgroundColor="#00ff0000" zPosition="4" />
                <eLabel position="406,777" size="350,8" backgroundColor="#0000ff00" zPosition="4" />
                <eLabel position="771,777" size="350,8" backgroundColor="#00ffff00" zPosition="4" />
                <eLabel position="1137,777" size="350,8" backgroundColor="#000000ff" zPosition="4" />
            </screen>"""


elif sz_w == 1920:
    if DreamOS():
        SKIN_full_main = """
            <screen position="center,center" size="1146,600" title="Flash And Full Backup" backgroundColor="#16000000" flags="wfNoBorder">
                <widget source="Title" render="Label" font="Regular;35" foregroundColor="#00bab329" position="28,5" size="1085,45" transparent="1" />
                <widget name="config" position="28,55" size="1085,280" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000" zPosition="1" />
                <widget source="help" render="Label" position="28,345" size="1082,130" font="Regular;28" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" transparent="1" zPosition="1" />
                <widget name="lab1" position="28,475" size="1085,63" font="Regular;30" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" zPosition="1" />
                <widget name="key_red" position="27,540" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_green" position="309,540" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_yellow" position="585,540" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_blue" position="861,540" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <eLabel position="28,580" size="250,8" backgroundColor="#00ff0000" zPosition="4" />
                <eLabel position="308,580" size="250,8" backgroundColor="#0000ff00" zPosition="4" />
                <eLabel position="584,580" size="250,8" backgroundColor="#00ffff00" zPosition="4" />
                <eLabel position="861,580" size="250,8" backgroundColor="#000000ff" zPosition="4" />
                </screen>
            """
    else:
        SKIN_full_main = """
            <screen position="center,center" size="1146,600" title="Flash And Full Backup" backgroundColor="#16000000" flags="wfNoBorder">
                <widget source="Title" render="Label" font="Regular;35" foregroundColor="#00bab329" position="28,5" size="1085,45" transparent="1" />
                <widget name="config" position="28,55" size="1085,280" font="Regular;30" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000" zPosition="1" />
                <widget source="help" render="Label" position="28,345" size="1082,130" font="Regular;28" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" transparent="1" zPosition="1" />
                <widget name="lab1" position="28,475" size="1085,63" font="Regular;30" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" zPosition="1" />
                <widget name="key_red" position="27,540" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_green" position="309,540" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_yellow" position="585,540" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_blue" position="861,540" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <eLabel position="28,580" size="250,8" backgroundColor="#00ff0000" zPosition="4" />
                <eLabel position="308,580" size="250,8" backgroundColor="#0000ff00" zPosition="4" />
                <eLabel position="584,580" size="250,8" backgroundColor="#00ffff00" zPosition="4" />
                <eLabel position="861,580" size="250,8" backgroundColor="#000000ff" zPosition="4" />
            </screen>"""


# 1280:
else:
    SKIN_full_main = """
        <screen position="center,center" size="902,400" title="Flash And Full Backup" backgroundColor="#16000000" flags="wfNoBorder">
            <widget source="Title" render="Label" font="Regular;35" foregroundColor="#00bab329" position="30,5" size="838,40" transparent="1" />
            <widget name="config" position="30,48" size="840,186" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000" />
            <widget source="help" render="Label" position="30,239" size="840,79" font="Regular;25" foregroundColor="#00ff2525" backgroundColor="#16000000" valign="center" transparent="1" zPosition="1" />
            <widget name="lab1" position="30,320" size="840,30" font="Regular;24" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" />
            <widget name="key_red" position="30,350" size="200,40" font="Regular; 24" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <widget name="key_green" position="244,350" size="200,40" font="Regular; 24" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <widget name="key_yellow" position="460,350" size="200,40" font="Regular; 24" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <widget name="key_blue" position="671,350" size="200,40" font="Regular; 24" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <eLabel position="30,389" size="200,4" backgroundColor="#00ff0000" zPosition="4" />
            <eLabel position="244,390" size="200,4" backgroundColor="#0000ff00" zPosition="4" />
            <eLabel position="461,391" size="200,4" backgroundColor="#00ffff00" zPosition="4" />
            <eLabel position="672,390" size="200,4" backgroundColor="#000000ff" zPosition="4" />
        </screen>"""


# doFlash screen
sz_w = getDesktop(0).size().width()
if sz_w == 2560:
    if DreamOS():
        SKIN_doFlash = """
            <screen name="Flash image" position="center,center" size="1528,979" title="Flash image" backgroundColor="#16000000" flags="wfNoBorder">
                <widget source="Title" render="Label" font="Regular;47" foregroundColor="#00bab329" position="27,7" size="1471,67" transparent="1" />
                <widget name="list" position="27,87" size="1471,698" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000" />
                <widget name="lab1" position="27,795" size="1486,114" font="Regular;47" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" />
                <widget name="key_red" position="40,910" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_green" position="406,910" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <eLabel position="40,960" size="350,8" backgroundColor="#00ff0000" zPosition="4" />
                <eLabel position="406,960" size="350,8" backgroundColor="#0000ff00" zPosition="4" />
            </screen>"""

    else:
        SKIN_doFlash = """
            <screen name="Flash image" position="center,center" size="1528,979" title="Flash image" backgroundColor="#16000000" flags="wfNoBorder">
                <widget source="Title" render="Label" font="Regular;47" foregroundColor="#00bab329" position="27,7" size="1471,67" transparent="1"/>
                <widget name="list" font="Regular;40" itemHeight="54" position="27,87" size="1471,698" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000"/>
                <widget name="lab1" position="27,795" size="1486,114" font="Regular;47" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" />
                <widget name="key_red" position="40,910" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <widget name="key_green" position="406,910" size="350,50" font="Regular;40" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
                <eLabel position="40,960" size="350,8" backgroundColor="#00ff0000" zPosition="4" />
                <eLabel position="406,960" size="350,8" backgroundColor="#0000ff00" zPosition="4" />
            </screen>"""


elif sz_w == 1920:
    if DreamOS():
        SKIN_doFlash = """
        <screen name="Flash image" position="center,center" size="1146,734" title="Flash image" backgroundColor="#16000000" flags="wfNoBorder">
            <widget source="Title" render="Label" font="Regular;35" foregroundColor="#00bab329" position="20,5" size="1103,50" transparent="1" />
            <widget name="list" position="20,65" size="1103,482" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000" />
            <widget name="lab1" position="20,570" size="1114,85" font="Regular;35" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" />
            <widget name="key_red" position="27,660" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <widget name="key_green" position="309,660" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <eLabel position="28,699" size="250,8" backgroundColor="#00ff0000" zPosition="4" />
            <eLabel position="310,701" size="250,8" backgroundColor="#0000ff00" zPosition="4" />
        </screen> """
    else:
        SKIN_doFlash = """
        <screen name="Flash image" position="center,center" size="1146,734" title="Flash image" backgroundColor="#16000000" flags="wfNoBorder">
            <widget source="Title" render="Label" font="Regular;35" foregroundColor="#00bab329" position="20,5" size="1103,50" transparent="1" />
            <widget name="list" position="20,65" size="1103,482" font="Regular;30" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000" />
            <widget name="lab1" position="20,570" size="1114,85" font="Regular;35" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" />
            <widget name="key_red" position="27,660" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <widget name="key_green" position="309,660" size="250,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <eLabel position="28,699" size="250,8" backgroundColor="#00ff0000" zPosition="4" />
            <eLabel position="310,701" size="250,8" backgroundColor="#0000ff00" zPosition="4" />
        </screen> """


# 1280: ok
else:
    SKIN_doFlash = """
        <screen position="center,center" size="902,400" title="Flash image" backgroundColor="#16000000" flags="wfNoBorder">
            <widget source="Title" render="Label" font="Regular;35" foregroundColor="#00bab329" position="30,5" size="838,40" transparent="1" />
            <widget name="list" position="31,45" size="841,250" scrollbarMode="showOnDemand" foregroundColor="#00ffffff" backgroundColor="#16000000" />
            <widget name="lab1" position="30,310" size="840,30" font="Regular;24" valign="center" foregroundColor="#00ffc435" backgroundColor="#16000000" transparent="1" />
            <widget name="key_red" position="30,350" size="200,40" font="Regular; 24" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <widget name="key_green" position="244,350" size="200,40" font="Regular; 24" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <eLabel position="30,389" size="200,4" backgroundColor="#00ff0000" zPosition="4" />
            <eLabel position="244,390" size="200,4" backgroundColor="#0000ff00" zPosition="4" />
        </screen>"""


# imagedownloadScreen screen
if sz_w == 2560:
    SKIN_imagedownloadScreen = """
        <screen name="imagedownloadScreen" position="center,center" size="1074,310" title="Downloading image..." backgroundColor="#16000000" flags="wfNoBorder">
            <widget name="activityslider" position="40,64" size="1007,40" borderWidth="2" transparent="1"/>
            <widget name="package" position="40,10" size="1007,47" font="Regular;36" halign="center" valign="center" transparent="1"/>
            <widget name="status" position="40,120" size="1007,54" font="Regular;32" halign="center" valign="center" transparent="1"/>
            <widget name="key_green" position="244,350" size="200,40" font="Regular; 24" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="#00ffffff" transparent="1" zPosition="1" />
            <eLabel text="Press Exit Button to cancel Downlaod" position="15,247" zPosition="2" size="1046,54" font="Regular;38" halign="center" valign="center" foregroundColor="#00ff2525" backgroundColor="#16000000"/>
        </screen>"""


elif sz_w == 1920:
    SKIN_imagedownloadScreen = """
        <screen name="imagedownloadScreen" position="center,center" size="805,232" title="Downloading image..." backgroundColor="#16000000" flags="wfNoBorder">
            <widget name="activityslider" position="30,48" size="755,30" borderWidth="1" transparent="1" />
            <widget name="package" position="30,7" size="755,35" font="Regular;27" halign="center" valign="center" transparent="1" />
            <widget name="status" position="30,90" size="755,40" font="Regular;24" halign="center" valign="center" transparent="1" />
            <widget name="key_green" position="15,144" size="780,40" font="Regular; 30" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="green" transparent="1" zPosition="1" />
            <eLabel text="Press Exit Button to cancel Downlaod" position="15,185" zPosition="2" size="780,40" font="Regular;28" halign="center" valign="center" foregroundColor="#00ff2525" backgroundColor="#16000000" />
        </screen>"""
# 1280:
else:
    SKIN_imagedownloadScreen = """
        <screen name="imagedownloadScreen" position="center,center" size="560,155" title="Downloading image..." backgroundColor="#16000000" flags="wfNoBorder">
            <widget name="activityslider" position="20,43" size="510,20" borderWidth="1" transparent="1" />
            <widget name="package" position="20,10" size="510,29" font="Regular;18" halign="center" valign="center" transparent="1" />
            <widget name="status" position="20,65" size="510,28" font="Regular;16" halign="center" valign="center" transparent="1" />
            <widget name="key_green" position="10,97" size="530,24" font="Regular; 23" halign="center" valign="center" backgroundColor="#30000000" foregroundColor="green" transparent="1" zPosition="1" />
            <eLabel text="Press Exit Button to cancel Downlaod" position="10,122" zPosition="2" size="530,24" font="Regular;23" halign="center" valign="center" foregroundColor="#00ff2525" backgroundColor="#16000000" />
        </screen>"""

# progress screen
if sz_w == 2560:
    SKIN_Progress = """
        <screen position="center,center" size="850,250" title="Command execution...">
            <widget name="text" position="14,14" size="820,175" font="Regular;24" />
            <widget name="slider" position="14,200" size="820,35" borderWidth="2" transparent="1" />
        </screen>"""

elif sz_w == 1920:
    SKIN_Progress = """
        <screen position="center,center" size="850,200" title="Command execution...">
            <widget name="text" position="10,10" size="825,160" font="Regular;24" />
            <widget name="slider" position="10,175" size="825,24" borderWidth="1" transparent="1" />
        </screen>"""


# 1280:
else:
    SKIN_Progress = """
        <screen position="center,center" size="550,155" title="Command execution...">
            <widget name="text" position="1,4" size="550,130" font="Regular;18" />
            <widget name="slider" position="0,137" size="550,20" borderWidth="1" transparent="1" />
        </screen>"""
