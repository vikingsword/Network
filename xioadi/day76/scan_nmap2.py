import nmap

# 创建一个 Nmap 扫描器对象
nm = nmap.PortScanner()

# 执行端口扫描
scan_results = nm.scan('127.0.0.1', '1-1000')

# 获取扫描结果
for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('Protocol : %s' % proto)

        ports = nm[host][proto].keys()
        for port in ports:
            print('Port : %s\tState : %s' % (port, nm[host][proto][port]['state']))
