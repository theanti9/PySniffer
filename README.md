PySniffer
=========
I plan to implement things such as logging, saving of packets that match a certain filter, etc. Currently, this is at a basic "It runs" point.

Dependencies
============
* [Scapy 2.x](http://www.secdev.org/projects/scapy/doc/installation.html) and its dependencies:
 * [libdnet (includes python wrapper)](http://code.google.com/p/libdnet/)
 * [libpcap](http://www.tcpdump.org/)
 * [pypcap (libpcap python wrapper)](http://code.google.com/p/pypcap/)

Caveats/Tips
============

Keep in mind that the python wrappers for libdnet and libpcap require the libraries to be installed before they will build.

When installing pypcap, if you get an error similar to the following:

llvm-gcc-4.2 -fno-strict-aliasing -fno-common -dynamic -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -mno-fused-madd -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -fwrapv -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch i386 -arch x86_64 -pipe -I/usr/include -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c pcap_ex.c -o build/temp.macosx-10.7-intel-2.7/pcap_ex.o
pcap_ex.c: In function ‘pcap_ex_fileno’:
pcap_ex.c:165: error: dereferencing pointer to incomplete type
pcap_ex.c: In function ‘pcap_ex_next’:
pcap_ex.c:253: error: dereferencing pointer to incomplete type
pcap_ex.c: In function ‘pcap_ex_fileno’:
pcap_ex.c:165: error: dereferencing pointer to incomplete type
pcap_ex.c: In function ‘pcap_ex_next’:
pcap_ex.c:253: error: dereferencing pointer to incomplete type

..it can be circumvented through patching your setup.py by adding the following line to the top of the file:

#define HAVE_PCAP_FILE

