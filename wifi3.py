import subprocess

def connect_to_wifi(ssid, password):
    try:
        # Disconnect if already connected to any network
        subprocess.run(['nmcli', 'networking', 'off'], check=True)
        subprocess.run(['nmcli', 'networking', 'on'], check=True)
        
        # Add new WiFi connection
        subprocess.run([
            'nmcli', 'dev', 'wifi', 'connect', ssid, 'password', password
        ], check=True)
        
        print(f"Connected to {ssid}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to {ssid}: {e}")

# Replace with your network's SSID and password
ssid = 'Your_SSID'
password = 'Your_PASSWORD'

connect_to_wifi(ssid, password)
