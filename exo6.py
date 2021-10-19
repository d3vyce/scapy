import argparse
from struct import pack
from sys import argv
from scapy.all import ARP, Ether, IP, srp

interface = iface=argv[2]
ip = iface=argv[3]

packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)

result = srp(packet, iface="en0", timeout=3, verbose=0)[0]

if result:
    for sent, received in result:
        print(received.hwsrc, " ", received.psrc)
