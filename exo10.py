import socket
from sys import argv
from typing import Protocol
from scapy.all import *

pcap = rdpcap("icmp.pcap")
i=1
tab = []

for packet in pcap:
    tab += [(i, packet[ICMP].type, packet.time, packet[ICMP].load)]
    i += 1
    
for pck in tab:
    if(pck[1] == 8):
        for packet in tab:
            if(packet[1] == 0 and packet[3] == pck[3]):
                id_rsp = packet[0]
                break
            id_rsp = "N/A"

        print(pck[0], "\t", id_rsp, "\t%.3f" %((packet[2]-pck[2])*1000), "ms")
