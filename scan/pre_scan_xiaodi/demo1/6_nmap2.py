import nmap

nmap_path = [r'E:\Sec\Tool\Scan\PortScan\Nmap\nmap-7.92\nmap.exe', ]
nm = nmap.PortScanner(nmap_search_path=nmap_path)
res = nm.scan(hosts='192.168.110.34/24', arguments='-T4 -F')
print(res)

res2 = nm.all_hosts()
print(res2)

res3 = nm.csv()
print(res3)
