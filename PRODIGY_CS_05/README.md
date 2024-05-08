# Network Packet Analyzer

This is a simple packet sniffer tool written in Python using the Scapy library. It captures and analyzes network packets, displaying relevant information such as source and destination IP addresses, protocols, and payload data.

## Features

- Captures network packets on a specified interface.
- Extracts source and destination IP addresses.
- Identifies the protocol used in each packet.
- Displays payload data (if available) in hexadecimal format.

## Requirements

- Python 3.x
- Scapy library (install using `pip install scapy`)

## Usage

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/network-packet-analyzer.git


2. Navigate to the project directory:

    ```sh
    cd network-packet-analyzer


3. Run the packet sniffer:

    ```sh
    python network_packet_analyzer.py


Replace `network_packet_analyzer.py` with the name of your script if different.

4. Enter the network interface name when prompted (e.g., `eth0` or `Ethernet`).

## Disclaimer

This tool is for educational purposes only. Use it responsibly and ensure you have the necessary permissions before capturing network packets.
