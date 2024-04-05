from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        # Display basic packet information
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {proto}", end='')

        # Further dissect TCP/UDP protocols for port information
        if TCP in packet:
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            print(f" | TCP: {tcp_sport} -> {tcp_dport}")
        elif UDP in packet:
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            print(f" | UDP: {udp_sport} -> {udp_dport}")
        else:
            print()

def main():
    print("Starting packet capture... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
