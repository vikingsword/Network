# !usr/bin/env python
# -*- coding:utf-8 _*-
import socks

for line in open('./ipv6_sender.txt'):
    line = line.strip()
    sock = socks.socksocket()
    sock.connect((line[0], line[1]))
    print(line)