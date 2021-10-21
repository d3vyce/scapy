import argparse
import os
from scapy.all import *

pcap = rdpcap("tftp.pcap")
i = 0
dst_port = 0
dst_addr = 0
buffer = ""

for pck in pcap:
    if(pck[Ether].type == 2048):
        if(pck[IP].proto == 17): 
            if(pck[UDP].dport == 69): 
                if(i > 0): 
                    print(f"{filename} : {i} packets ({dst_addr}:{dst_port})")
                    if('/' in filename):
                        if not os.path.exists(os.path.dirname(filename)):
                            os.makedirs(os.path.dirname(filename))
                    with open(filename, 'w') as file:
                        file.write(buffer)
                        buffer = ""
                dst_port = pck[UDP].sport
                dst_addr = pck[IP].src
                filename = pck[TFTP].filename.decode("utf-8")
                i = 0
            elif("File Not Found" in pck.sprintf("%load%")):
                print(f"{filename} : File Not Found")
            elif(pck[UDP].dport == dst_port and pck[IP].dst == dst_addr and "blksize" not in pck.sprintf("%load%")): 
                buffer += pck[Raw].load.decode('utf-8', 'replace')
                i += 1