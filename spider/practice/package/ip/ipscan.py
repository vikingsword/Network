import socket


def scan_port(ip, port):
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(0.01)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"Port {port} is open on {ip}")
            with open('ip.txt', 'a+') as f:
                f.write(ip)

        sock.close()
    except socket.error:
        print(f"Could not connect to {ip}")


port = 80
for i in range(0, 256):
    for j in range(0, 256):
        for k in range(0, 256):
            ip = f"198.{i}.{j}.{k}"
            scan_port(ip, port)
