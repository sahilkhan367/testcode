import os
import subprocess
import time

def write_wpa_supplicant_conf(ssid, password):
    config_content = f"""
    network={{
        ssid="{ssid}"
        psk="{password}"
    }}
    """
    with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as conf_file:
        conf_file.write(config_content)

def start_wpa_supplicant(interface):
    try:
        # Bring up the interface
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'], check=True)
        
        # Start wpa_supplicant
        subprocess.run(['sudo', 'wpa_supplicant', '-B', '-i', interface, '-c', '/etc/wpa_supplicant/wpa_supplicant.conf'], check=True)
        
        # Request an IP address
        subprocess.run(['sudo', 'dhclient', interface], check=True)
        print(f"Successfully connected to {ssid}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print("Check if wpa_supplicant is installed and the network interface is correct.")

# Input SSID and Password
ssid = input("Enter the SSID of the network: ")
password = input("Enter the password: ")

# Write configuration
write_wpa_supplicant_conf(ssid, password)

# Wait to ensure wpa_supplicant has time to process the configuration
time.sleep(5)

# Start connection process
interface = 'wlan0'  # Replace with your wireless interface
start_wpa_supplicant(interface)
