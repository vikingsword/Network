import socket

import nmap
import whois


# nm = nmap.PortScanner()
# nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]

ip = socket.gethostbyname('www.baidu.com')
print(ip)
res = whois.whois('www.baidu.com')
print(res)

scanner = nmap.PortScanner()
res = scanner.scan(ip + '-100', '80', '-sV')
print(res)
