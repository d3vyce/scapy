import os
from scapy.all import *

pcap = rdpcap("tftp.pcap")
i = 0
dst_port = 0
buffer = ""

for pck in pcap:
    if(pck[Ether].type == 2048):        # Check for type=IPv4
        if(pck[IP].proto == 17):        # Check for proto=udp
            if(pck[UDP].dport == 69):   # Check for dport=tftp
                if(i > 0):              # Check fin de transfert
                    print(f"{filename} : {i} packets (Port : {dst_port})")
                    if('/' in filename):    # Check si le fichier est dans un dossier
                        if not os.path.exists(os.path.dirname(filename)):   # Check si le dossier n'existe pas
                            os.makedirs(os.path.dirname(filename))          # Si oui creer le dossier
                    with open(filename, 'w') as file:   # Creation du fichier
                        file.write(buffer)              # Ecriture du buffer dans le fichier
                        buffer = ""                     # Reset buffer
                dst_port = pck[UDP].sport
                filename = pck[TFTP].filename.decode("utf-8")
                i = 0
            elif("File Not Found" in pck.sprintf("%load%")):    # Check que le request concerne un fichier existant
                print(f"{filename} : File Not Found")
            elif(pck[UDP].dport == dst_port and "blksize" not in pck.sprintf("%load%")): # Check que c'est un packet DATA et non un accuse de réception
                buffer += pck[Raw].load.decode('utf-8', 'replace') # Conversion du load (byte) en str avec remplacement des caracteres inexistant + stockage dans buffer
                i += 1