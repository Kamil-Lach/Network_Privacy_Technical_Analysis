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

## 📁 Repository Structure
- `Analiza_porownawcza.pdf`: The full technical report (in Polish).[Analiza_porownawcza.pdf](https://github.com/user-attachments/files/27015701/Analiza_porownawcza.pdf)

---
*Created as part of a deep-dive study into network protocols and cybersecurity.*
