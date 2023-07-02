import os
import socket


def getIpByHost(hostName):
    ip = socket.gethostbyname(hostName)
    print(ip)


if __name__ == '__main__':
    # hostName = input('input host: ')
    # getIpByHost(hostName)

    command = input('input your command: ')
    result = os.system('nslookup ' + command)
    print(result)




