# Network Anonymization Analysis: Direct vs. VPN vs. Proxy vs. TOR

## 📌 Project Overview
This project is a detailed technical study of how different network connection methods impact user privacy and traffic metadata. I conducted a series of controlled tests using an isolated Virtual Machine environment to capture and analyze network packets, browser fingerprints, and potential data leaks.

The goal was to document the transition from a completely transparent "Direct" connection to highly anonymized "TOR" traffic, analyzing the changes at the packet level (OSI Layer 2-4) and application level (Layer 7).

## 🛠 Tools & Environment
- **Environment:** Isolated Virtual Machine (VM)
- **Traffic Analysis:** Wireshark
- **Fingerprinting Tools:** BrowserLeaks, Tor Relay Search, WHOIS Lookups
- **Operating System:** Linux-based testing environment

## 🔍 Key Technical Findings

### 📶 Direct Connection
- **Privacy:** None. ISP and destination servers see the real public IP, location, and owner details (via WHOIS).
- **Traffic:** DNS queries are sent in plaintext (UDP port 53), making browsing history visible to the network administrator.
- **Fingerprint:** Standard MTU (1500) and unmasked JA3/TLS fingerprints.

### 🛡 VPN (Virtual Private Network)
- **Encapsulation:** All traffic (DNS, HTTP, ICMP) is bundled into a single encrypted tunnel (SSL/TLS).
- **Packet Analysis:** Wireshark shows only "Continuation Data" directed to the VPN server IP.
- **Key Observation:** MTU is reduced to **1426** due to the overhead of the VPN tunnel encapsulation.

### 🌐 Proxy (HTTP/HTTPS)
- **Vulnerability:** Exposed to **WebRTC leaks**, which can reveal the real local and public IP address despite the proxy.
- **Packet Analysis:** Visible `HTTP CONNECT` frames in Wireshark, revealing the destination domain even if the payload is encrypted.
- **Verdict:** Least secure method for overall anonymity.

### 🧅 TOR (The Onion Router)
- **Anonymity:** Multi-layer encryption through Entry, Middle, and Exit nodes.
- **Traffic Profile:** Identifiable by communication with Entry Guards on port 9001 and specific packet frequency patterns.
- **Technical Detail:** Maintains a standard MTU of 1500 but introduces higher latency due to multi-hop routing.

## 🛡 OPSEC & Data Privacy
For the purpose of this public repository, all sensitive information has been redacted to follow **Operational Security (OPSEC)** best practices:
- Public and Local IP addresses are masked.
- Hardware identifiers (MAC addresses) in Wireshark hex dumps are blacked out.
- Personal data in WHOIS records has been removed.

### 🚀 Installation & Setup
To run the included IP analysis tool, you need Python 3.x installed on your system.

Required Libraries:
The script requires the requests library with SOCKS5 support to route traffic through the Tor network. Install it via your terminal:

pip install requests[socks]

Tor Service (Optional): If you want to test the Tor routing feature (Option 2 in the script), you must have the Tor service running locally on port 9050 (e.g., using sudo systemctl start tor on Linux).

### 📁 Repository Structure & File Roles

### ⚠️ CRITICAL: For the Python script to function correctly, all related files (Github_project.py, blacklist.txt, and the generated IP_log.txt) MUST be located in the exact same folder.

- **IP_Analyzer.py:** The main automation script. It acts as a CLI tool that fetches your current IP data (via ip-api.com), allows you to route requests normally or through Tor, and performs a security check to determine if your connection is being masked.

- **blacklist.txt:** A local database file containing keywords associated with VPN providers, datacenters, cloud hosts, and Tor nodes (e.g., OVH, NordVPN, M247, Stiftung). The script cross-references your detected ISP name against this list to flag anonymized traffic.

- **IP_log.txt:** An automatically generated text file created by the script upon its first run. It securely stores a local history of your connection tests, logging the timestamp, IP address, ISP name, and location for each session.

- **.gitignore:** A vital Git configuration file. It ensures that sensitive local data (like the IP_log.txt file containing your real IP address) and Python temporary cache files (__pycache__) are completely ignored and not uploaded to your public GitHub repository.

### 📸 Visual Analysis (Screenshots)

This repository contains screenshots demonstrating the script's behavior across different network setups:

- **Direct.png:** The user selects Option 1 (Direct Connection). The script fetches the IP and identifies the ISP (e.g., "**********"). Since this specific ISP name isn't found in blacklist.txt, the tool correctly identifies it as a standard "Residential ISP" (Direct connection).

<img width="518" height="258" alt="Direct" src="https://github.com/user-attachments/assets/956b2297-e8e4-49d3-bad5-76789d2b1cb2" />

- **VPN.png:** The user runs the script while connected to a VPN. The ISP changes to "OVH SAS". The script scans blacklist.txt, detects the keyword "OVH" (a known server provider), and issues a security warning: "Your ISP suggests you might be using a VPN or proxy."

<img width="512" height="273" alt="VPN" src="https://github.com/user-attachments/assets/236fe4fb-0c08-40fc-8641-e9cf8f269bb8" />

- **TOR.png:** The user selects Option 2 (Tor Routing). The traffic is routed through the local localhost:9050 proxy. The IP shifts to a German exit node ("Stiftung Erneuerbare Freiheit"). The blacklist catches the keyword "Stiftung" and successfully flags the connection.

<img width="515" height="256" alt="TOR" src="https://github.com/user-attachments/assets/bbec069f-2602-4490-8141-7876dbf52de1" />

- **Saved_logs.png:** A peek inside the auto-generated IP_log.txt file, showing how the script chronologically logs each session's timestamp, IP, ISP, and location for easy historical tracking.

<img width="937" height="205" alt="Saved_logs" src="https://github.com/user-attachments/assets/2e6868be-4e8d-48ec-b527-e7066e054528" />

### 📁 Repository Structure

| File | 
| :--- | 
| 🐍 [IP_Analyzer.py](https://github.com/user-attachments/files/27307783/IP_Analyzer.py) |
| The main Python CLI tool. |
| 🛡️ Downald in my repositories file name: .gitignore |
|A vital Git configuration file. It ensures that sensitive local data (like the IP_log.txt file) and Python temporary cache files (__pycache__) are completely ignored and not uploaded to your public GitHub repository.
| 🛑 [blacklist.txt](https://github.com/user-attachments/files/27307802/blacklist.txt) |
| Keyword database for VPN/Tor detection. |
| 📄 [Analiza_porownawcza.pdf](https://github.com/user-attachments/files/27307805/Analiza_porownawcza.pdf) |
| **The full technical report (in Polish).** |
---
*Created as part of a deep-dive study into network protocols and cybersecurity.*
