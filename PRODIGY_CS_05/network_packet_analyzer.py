import scapy.all as scapy

def packet_sniffer(interface):
    try:
        scapy.sniff(iface=interface, store=False, prn=process_packet)
    except Exception as e:
        print(f"Error: {e}")

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        payload = packet[scapy.Raw].load if packet.haslayer(scapy.Raw) else None

        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol}")
        if payload:
            print(f"Payload Data: {payload.hex()}")  # Display payload data in hexadecimal format

# Usage
interface = "Ethernet"  # Update this with your actual network interface name
packet_sniffer(interface)
