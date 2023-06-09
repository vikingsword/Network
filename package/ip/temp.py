ip = "192.168.0.0"
with open('ip.txt', 'a+') as f:
    f.write(str(ip))
f.close()
