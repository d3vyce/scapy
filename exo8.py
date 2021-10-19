import socket
from sys import argv
from scapy.all import ICMP , IP, TCP, UDP
import scapy.sendrecv

protocol = argv[1]
hostname = argv[2]
host = socket.gethostbyname(hostname)
port = argv[3]

print(hostname, " -> ", host)

if(protocol == "ICMP"): packet = IP(dst=host, ttl = (1,20))/ICMP(type='echo-request')
elif(protocol == "TCP"): packet = IP(dst=host, ttl = (1,20))/TCP(dport=int(port), flags="S")
elif(protocol == "UDP"): packet = IP(dst=host, ttl = (1,20))/UDP(dport=int(port))

for pkt in packet:
    result = scapy.sendrecv.sr1(pkt, verbose=False, timeout=2)
    if(result == None): print("TTL \t", pkt[0].ttl, "\t****\t", protocol)
    else: 
        print("TTL \t", pkt[0].ttl, "\t", result[0].src, "\t", protocol)
        if(result[0].src == host): break
