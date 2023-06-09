import socket


def scan_port(ip, port):
    try:
        # 创建socket对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间（可选）
        sock.settimeout(0.01)
        # 尝试连接IP的指定端口
        result = sock.connect_ex((ip, port))
        print(f"scanning {ip}", ip)
        if result == 0:
            print(f"Port {port} is open on {ip}")
            with open('ip.txt', 'wb') as f:
                f.write(ip)
        # 关闭socket连接
        sock.close()
    except socket.error:
        print(f"Could not connect to {ip}")


# 扫描示例：扫描10.0.0.0到10.255.255.255范围内的80端口
port = 80
for i in range(0, 256):
    for j in range(0, 256):
        for k in range(0, 256):
            ip = f"10.{i}.{j}.{k}"
            scan_port(ip, port)
