import os
import socket

import whois as whois


def getIpByHost(hostName):
    ip = socket.gethostbyname(hostName)
    print(ip)
    return ip


def get_whois(url):
    data = whois(url)
    print(data)


if __name__ == '__main__':

    # 域名反查ip
    # hostName = input('input host: ')
    # getIpByHost(hostName)

    # 识别目标是否存在cdn：nslookup
    # command = input('input your command: ')
    # res = os.popen('nslookup ' + command)
    # dot_num = res.read().count('.')
    # if dot_num > 10:
    #     print('exist')
    # else:
    #     print('absent')

    # 端口扫描：
    # 1. 原生自写socket协议tcp，udp扫描 - v1
    # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = input('input your host: ')
    # port = int(input('input your port: '))
    # ip = getIpByHost(host)
    # res = server.connect_ex((ip, port))
    # if res == 0:
    #     print('this port is open ')
    # else:
    #     print('this port is close')

    # 原生自写socket协议tcp，udp扫描 - v2
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input('input your host: ')
    ports = {20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 8080, 8443, 8888}
    for port in ports:
        ip = getIpByHost(host)
        res = server.connect_ex((ip, port))
        if res == 0:
            print(port, ' port is open ')
        else:
            print(port, ' port is close')

    # 2. 调用第三方模块扫描
    # 3. 调用系统工具脚本执行












