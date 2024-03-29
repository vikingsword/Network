import nmap


def scan(host):
    nm = nmap.PortScanner()
    nm.scan(hosts=host, arguments='-p 1-1000')

    for host in nm.all_hosts():
        print(f'Host: {host}')
        for proto in nm[host].all_protocols():
            print(f'Protocol: {proto}')
            ports = nm[host][proto].keys()
            for port in ports:
                print(f'Port: {port}, State: {nm[host][proto][port]["state"]}')


if __name__ == "__main__":
    target_host = "127.0.0.1"
    scan(target_host)
