import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.config import conf
from scapy.all import sniff

import settings

conf = settings.conf

def callback(pkt):
	print `pkt`, '\n\n'

def main():
	sniff(prn=callback, filter="", store=0)

if __name__ == '__main__':
	main()