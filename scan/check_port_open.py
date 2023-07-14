import socket


def check_ssh_port(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # 设置超时时间为2秒
    result = sock.connect_ex((ip, 22))
    if result == 0:
        print(f"Port 22 is open on {ip}")
    else:
        print(f"Port 22 is closed on {ip}")
    sock.close()


# 示例用法
ip_address = "198.148.127.47"  # 要检测的IP地址
check_ssh_port(ip_address)
