import socket
from sys import argv
from scapy.all import ICMP , IP
import scapy.sendrecv

hostname = argv[1]
host = socket.gethostbyname(hostname)

print(hostname, " -> ", host)
packet = IP(dst=host, ttl = (1,20))/ICMP(type='echo-request')

for pkt in packet:
    result = scapy.sendrecv.sr1(pkt, verbose=False, timeout=2)
    if(result == None): print("TTL \t", pkt[0].ttl, "\t****\t ICMP")
    else: 
        print("TTL \t", pkt[0].ttl, "\t", result[0].src, "\t ICMP")
        if(result[0].src == host): break
