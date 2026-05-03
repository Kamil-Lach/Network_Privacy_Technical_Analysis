import requests
from datetime import datetime
import time
import os

# Load ISP blacklist from a local file to identify potential VPN/proxy usage.
base_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_path, 'blacklist.txt')
with open(config_path, 'r') as f:
    blacklist = [line.strip().lower() for line in f if line.strip()]

def get_public_ip(use_tor=False):
    """Fetch public IP data, optionally via TOR SOCKS5 proxy."""
    proxies = None
    if use_tor:
        # Use SOCKS5 to prevent DNS leaks.
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }

    try:
        r= requests.get('http://ip-api.com/json/', proxies=proxies, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def main():
    # User interface for connection type selection.
    print("Started IP check...")
    print("1. Direct Connection (Standard)")
    print("2. Using Tor (Requires Tor to be running on localhost:9050)")

    choice = input("Choose connection type (1 or 2): ")
    
    # Execute IP check based on user choice.
    if choice == '2':
        print("Checking IP via Tor...")
        data = get_public_ip(use_tor=True)
    else:
        print("Checking Direct IP...")
        data = get_public_ip(use_tor=False)

    # Analyze and log results.
    if "error" not in data:
        print("IP check successful.")
    
        # Extracting data from ip-api response.
        ip = data.get('query')
        isp = data.get('isp')
        country = data.get('country')
        city = data.get('city')

        print(f"Public IP: {ip}, ISP: {isp}")
        print(f"Country: {country}, City: {city}")

        # Logging results to a local text file with a timestamp.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - IP: {ip}, ISP: {isp}, Country: {country}, City: {city}\n"

        log_path = os.path.join(base_path, "IP_log.txt")

        try: 
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
            print("IP information logged successfully.")
            print(f"[+] Data saved to: {os.path.abspath('log_path')}")
        except Exception as e:
            print(f"Error logging IP information: {e}")

        # Basic security analysis based on ISP information.
        print("\n--- Security Analysis ---")
        
        if any(keyword in isp.lower() for keyword in blacklist):
            print("Warning: Your ISP suggests you might be using a VPN or proxy.")
        else:
            print("Connection seems to be Direct (Residential ISP).")
    
    # Display error message if the API request failed.
    else:
        print(f"\n[!] Connection Error: {data['error']}")
        print("If you chose Tor, make sure Tor is running and configured correctly.")

    # Pause before exiting to allow user to read results.
    time.sleep(30)
        
if __name__ == "__main__":
    main()
