# -*- coding: utf-8 -*-

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import os,gettext

PluginLanguageDomain = "ShowClock"
PluginLanguagePath = "Extensions/ShowClock/locale"

def localeInit():
	lang = language.getLanguage()[:2] # getLanguage returns e.g. "fi_FI" for "language_country"
	os.environ["LANGUAGE"] = lang # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
	#print "[WebInterface] set language to ", lang
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))

def _(txt):
	t = gettext.dgettext(PluginLanguageDomain, txt)
	if t == txt:
		#print "[%s] fallback to default translation for %s" %(PluginLanguageDomain, txt)
		t = gettext.gettext(txt)
	return t

localeInit()
language.addCallback(localeInit)
