'''
python multicast_mac.py 239.0.0.1
Multicast IP: 239.0.0.1
Multicast MAC: 01:00:5E:00:00:01
'''
import re
import sys

def ip_to_mac(ip_address):
    # Convert multicast IP to MAC
    ip_parts = [int(x) for x in ip_address.split('.')]
    mac = [0x01, 0x00, 0x5E]  # Multicast MAC address prefix
    mac.extend(ip_parts[1:4])  # Append last 3 octets of IP address
    return ':'.join(['%02X' % x for x in mac])

# Replace '239.0.0.1' with your multicast IP address
multicast_ip = sys.argv[1]
multicast_mac = ip_to_mac(multicast_ip)

print(f"Multicast IP: {multicast_ip}")
print(f"Multicast MAC: {multicast_mac}")
