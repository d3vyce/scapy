import argparse
from struct import pack
from sys import argv
from scapy.all import ARP, Ether, IP, srp

interface = iface=argv[1]
ip = iface=argv[2]

packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)

result = srp(packet, iface=interface, timeout=3, verbose=0)[0]

if result:
    for sent, received in result:
        print(received.hwsrc, " ", received.psrc)
