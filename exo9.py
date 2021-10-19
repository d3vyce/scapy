import socket
from sys import argv
from typing import Protocol
from scapy.all import *

protocol = argv[1]
ip = argv[2]
portmin = argv[3]
portmax = argv[4]

if(protocol == "TCP"): packet = IP(dst=ip)/TCP(sport=55555, dport=(int(portmin), int(portmax)),  flags="S")
elif(protocol == "UDP"): packet = IP(dst=ip)/UDP(sport=55555, dport=(int(portmin), int(portmax)),  flags="S")

for pkt in packet:
    result = sr1(pkt, verbose=False, timeout=1)
    if(result == None): continue
    if("S" in result[TCP].flags): print(protocol, "\t", pkt[0].dport, "\topen")
    elif("R" in result[TCP].flags): print(protocol, "\t", pkt[0].dport, "\tclosed")
