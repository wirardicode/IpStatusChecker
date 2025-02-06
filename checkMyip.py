import socket
import psutil
#from scapy.all import ARP, Ether, srp  # Perlu pustaka scapy

def get_all_network_interfaces():
    interfaces = psutil.net_if_addrs()
    ip_details = {}
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == socket.AF_INET:  # IPv4 address
                ip_details[interface_name] = address.address
    return ip_details

#def show_who_inNetwork():
#    # Mendapatkan IP dan subnet perangkat lokal
#    interfaces = psutil.net_if_addrs()
#    local_ip = None
#    for iface, iface_addresses in interfaces.items():
#        for address in iface_addresses:
#            if address.family == socket.AF_INET:
#                local_ip = address.address
#                netmask = address.netmask
#                break
#        if local_ip:
#            break
#    
#    if not local_ip or not netmask:
#        return "Tidak dapat mendeteksi jaringan lokal."
#
#    # Hitung subnet
#    ip_parts = local_ip.split('.')
#    subnet = '.'.join(ip_parts[:3]) + '.0/24'  # Asumsi subnet /24 (255.255.255.0)
#
#    # Melakukan pemindaian jaringan
#    print(f"Memindai jaringan pada subnet: {subnet}")
#    arp = ARP(pdst=subnet)
#    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
#    packet = ether / arp
#    result = srp(packet, timeout=3, verbose=0)[0]
#
#    devices = []
#    for sent, received in result:
#        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
#
#    return devices

# Menampilkan semua antarmuka jaringan dan IP-nya
ips = get_all_network_interfaces()
print("Semua IP pada antarmuka jaringan:")
for interface, ip in ips.items():
    print(f"{interface}: {ip}")

# Menampilkan semua perangkat yang terhubung di jaringan
#devices = show_who_inNetwork()
#print("\nPerangkat yang terhubung di jaringan:")
#for device in devices:
#    print(f"IP: {device['ip']}, MAC: {device['mac']}")
