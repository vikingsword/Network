import os
import socket
import subprocess

domain = 'www.xiaodi8.com'
ip = socket.gethostbyname(domain)
# print(ip)

# res = os.system('nslookup ' + ip)
# print(res)

# res = subprocess.Popen('nslookup ' + domain)
# print(res)

res = os.popen('nslookup ' + domain).read()
print(res)
count = res.count('.')
print(count)