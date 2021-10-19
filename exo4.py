import ieee
import argparse
from scapy.all import *

parser = argparse.ArgumentParser()
parser.add_argument("-i")
args = parser.parse_args()

print("Listening on:", args.i)


known_mac = []

ieee_parser = ieee.IEEEParser()

def on_packet_received(packet):

    #Check if mac is known
    mac = packet[0].src
    if mac not in known_mac:
        known_mac.append(mac)

        #Find mac in database
        result = ieee_parser.search_constructor(mac)

        #Display result
        if (result):
            print(mac, " : ", result)
        else:
            print(mac, " :  No constructor found")
    return None

#Call on_packet_received on each packet captured
sniff(iface=args.i, prn=on_packet_received)
