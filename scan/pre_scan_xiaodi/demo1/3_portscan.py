import socket

target = 'www.bilibili.com'
ip = socket.gethostbyname(target)

for port in range(1, 1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    res = sock.connect_ex((ip, port))
    if res == 0:
        print('server: ' + str(ip) + '    port: ' + str(port) + ' open')
    # else:
    #     print('close')

#