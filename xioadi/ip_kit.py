import os
import socket
import sys

import whois


def getIpByHost(url):
    # 域名反查ip
    ip = socket.gethostbyname(url)
    print(url + '的 ip 为： ' + ip)
    return ip


def get_whois(url):
    data = whois(url)
    print(data)


def get_cdn(url):
    # 识别目标是否存在cdn：nslookup
    res = os.popen('nslookup ' + url)
    dot_num = res.read().count('.')
    if dot_num > 10:
        print('存在 cdn')
    else:
        print('不存在 cdn')


def port_scan(url):
    # 原生自写socket协议tcp，udp扫描
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input('input your host: ')
    ports = {20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 8080, 8443, 8888, 3306, 5432, 6379, 27017,
             1521}
    for port in ports:
        ip = socket.gethostbyname(url)
        res = server.connect_ex((ip, port))
        if res == 0:
            print(port, '   open ')
        else:
            print(port, '   close')


if __name__ == '__main__':
    # 例如 python ip_kit.py -u -t 中
    # argv[0]   -->     ip_kit.py
    # argv[1]   -->     -u
    # argv[2]   -->     -t  依次类推
    file = sys.argv[0]
    param1 = sys.argv[1]
    param2 = sys.argv[2]
    param3 = sys.argv[3]

    if param1 == '-u' and param3 == '-c':
        # cdn
        get_cdn(param2)
    if param1 == '-u' and param3 == '-ip':
        getIpByHost(param2)
