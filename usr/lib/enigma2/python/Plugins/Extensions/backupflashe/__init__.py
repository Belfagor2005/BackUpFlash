# -*- coding: utf-8 -*-

from __future__ import absolute_import
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import gettext
import os


PluginLanguageDomain = 'backupflashe'
PluginLanguagePath = 'Extensions/backupflashe/locale'
DBACKUP = resolveFilename(SCOPE_PLUGINS, 'Extensions/dBackup')
PLUGINROOT = resolveFilename(SCOPE_PLUGINS, 'Extensions/backupflashe')

if os.path.exists(DBACKUP) and not os.path.exists(DBACKUP + '/tools/version'):
    os.system('rm -r %s' % DBACKUP)

isDreambox = False
if os.path.exists("/usr/bin/apt-get"):
    isDreambox = True


def localeInit():
    if isDreambox:
        lang = language.getLanguage()[:2]
        os.environ["LANGUAGE"] = lang
    gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


if isDreambox:
    def _(txt):
        return gettext.dgettext(PluginLanguageDomain, txt) if txt else ""
else:
    def _(txt):
        translated = gettext.dgettext(PluginLanguageDomain, txt)
        if translated:
            return translated
        else:
            print(("[%s] fallback to default translation for %s" % (PluginLanguageDomain, txt)))
            return gettext.gettext(txt)

localeInit()
language.addCallback(localeInit)
