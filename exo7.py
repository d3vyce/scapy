import socket
from sys import argv
from scapy.all import ICMP , IP
import scapy.sendrecv

hostname = argv[1]

packet = IP(dst=hostname, ttl = (1,20))/ICMP(type='echo-request')

for pkt in packet:
    result = scapy.sendrecv.sr1(pkt, verbose=False, timeout=2)
    if(result == None): print("TTL \t", pkt[0].ttl, "\t****\t ICMP")
    else: 
        print("TTL \t", pkt[0].ttl, "\t", result[0].src, "\t ICMP")
        if(result[0].src == socket.gethostbyname(hostname)): break
