import json
import netmiko
import time
import signal
import sys
from netaddr import EUI, mac_cisco

if len(sys.argv) != 5:
    print('Usage: python MAC_finder.py <ip_list_file> <mac_address> <username> <password>')
    exit(1)

# Command-line arguments
ip_list_file = sys.argv[1]
mac_address = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

# Validate MAC address format and convert to Cisco-style MAC
try:
    mac_address = str(EUI(mac_address, dialect=mac_cisco))
except ValueError:
    print("Invalid MAC address format. Please provide a valid MAC address.")
    exit(1)

# Read the list of IP addresses from the file
try:
    with open(ip_list_file, 'r') as file:
        ips = file.readlines()
except FileNotFoundError:
    print(f"File '{ip_list_file}' not found. Please provide a valid IP list file.")
    exit(1)

logfile = 'log.log'
log = open(logfile, mode='a+')

for ip in ips:
    try:
        ip = ip.strip()
        print("*" * 75)
        print(ip)
        connection = netmiko.ConnectHandler(ip, device_type='cisco_ios', username=username, password=password)
        connection.secret = ''
        print(connection.base_prompt)
        connection.enable()

        output = connection.send_command(f"show mac address-table | include {mac_address}")
        if output != "":
            hostname = connection.base_prompt
            print(hostname)
            print(output)
        connection.disconnect()

    except Exception as e:
        print(str(e))
        log.write(str(e) + '\n')

log.close()
