import argparse
from scapy.all import *

pcap = rdpcap("icmp.pcap")

for packet in pcap:
    break