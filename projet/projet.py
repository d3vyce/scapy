import argparse
from scapy.all import *

pcap = rdpcap("tftp.pcap")
i = 0
dst_port = 0
dst_addr = 0

print(pcap[9].show())
print(pcap[9][Raw].load)


for pck in pcap:
    if(pck[Ether].type == 2048):
        if(pck[IP].proto == 17): 
            if(pck[UDP].dport == 69): 
                if(i > 0): print(f"{filename} : {i} packets ({dst_addr}:{dst_port})")
                dst_port = pck[UDP].sport
                dst_addr = pck[IP].src
                filename = pck[TFTP].filename
                i = 0
            elif("File Not Found" in pck.sprintf("%load%")):
                print(f"{filename} : File Not Found")
            elif(pck[UDP].dport == dst_port and pck[IP].dst == dst_addr and "blksize" not in pck.sprintf("%load%")): 
                i += 1