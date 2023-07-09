import socket
import nmap


# 文件名不能是nmap.py 否则会导致循环引入
# ip = socket.gethostbyname('www.xiaodi8.com')
# scanner = nmap.PortScanner()
# res = scanner.scan(ip + '-100', '80', '-sV')
# print(res)

def nmapscan():
    nm = nmap.PortScanner()
    try:
        data = nmap.scan(host='192.168.110.34/24', arguments='-T4 -F')
        print(nm.all_hosts())
        print(nm.csv())
        print(data)
    except Exception as e:
        print('error')


if __name__ == '__main__':
    nmapscan()