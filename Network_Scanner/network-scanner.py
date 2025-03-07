import scapy.all as scapy
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-s", "--scan", dest="scan", help="IP / Range of IP address to scan")
    (options, arguments) = parser.parse_args()
    if not options.scan:
        parser.error("[-] Please specify IP / IP Range  ,use --help for info")
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list


def print_result(client_list):
    print("IP\t\t\tMAC ADDRESS\n------------------------------------------")
    for client in client_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_result = scan(options.scan)
print_result(scan_result)
