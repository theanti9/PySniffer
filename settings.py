from scapy.config import conf as dconf
from scapy.themes import *

## Settings
#
settings = {
	'iface':			"en1", 	# Hardware interface to listen on
	'sniff_promisc':	True,	# Whether of not to use promiscuous mode
	'ipv6_enabled':	False,  # Whether or not to get ipv6 packets
	'color_theme':	DefaultTheme,
}

# Availible themes for color_theme setting:
# DefaultTheme, NoTheme, ColorPrompt, LatexTheme, BlackAndWhite, FormatTheme, HTMLTheme2, AnsiColorTheme, HTMLTheme, RastaTheme, ColorTheme, ColorOnBlackTheme, LatexTheme2, BrightTheme

#################

settings['color_theme'] = settings['color_theme']()

conf = dconf
for s in settings:
	if hasattr(conf, s):
		print s
		setattr(conf, s, settings[s])
