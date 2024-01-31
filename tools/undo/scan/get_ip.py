import socket


def getIp(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None


if __name__ == '__main__':
    domain = input('please input your domain: ')
    ip = getIp(domain)
    print(str(ip))
