#!/usr/bin/env python
# -\*- coding: utf-8 -\*-
from scapy.all import *

r = rdpcap("dog_catcher.pcap")
l = len(r)
print l
D = []
for i in range(0, l):
    if ICMP in r[i]:
        print 'OK'
        print r[i][ICMP].summary()
        if r[i][ICMP].type == 8 : # ICMP request
            d = str(r[i][Raw]).encode('hex')
            if d not in D:
                D.append(d)

f = open('bin', 'w')
f.write(''.join(D).decode("hex"))
f.close()
