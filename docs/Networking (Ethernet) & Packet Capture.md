# Networking (Ethernet) & Packet Capture
```bash
isi networks list interfaces -v
isi network groupnets list
isi network subnets list
isi network pools list
```

**ARP**
```bash
arp -an; arp -da; arp -an
```

**Cluster‑wide tcpdump**
```bash
isi_for_array -X 'for i in $(ifconfig | grep -B2 ether | grep flags | egrep -v "laggport|lo0|ISIINTERNAL" | cut -d: -f1); do   tcpdump -i ${i} -s320 -w /ifs/data/Isilon_Support/`hostname`.${i}_$(date +%m%d%Y_%H%M%S).pcap & done' &>/dev/null &
```
