import socket


def port_scan(url):
    # 原生自写socket协议tcp，udp扫描
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    url = 'www.xiaodi8.com'
    port_scan(url)
