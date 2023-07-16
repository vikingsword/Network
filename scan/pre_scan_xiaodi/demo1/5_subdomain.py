import socket
import sys
import time


def getSubDomain(url):
    domain = url.replace('www', '')
    for data in open('E:\Sec\Tool\Mess\Dict\PasswordDic-master\SubDomain.dic'):
        data = data.replace('\n', '')
        subdomain = data + domain
        # print(subdomain)
        try:
            ip = socket.gethostbyname(subdomain)
            print(subdomain + '--> ' + ip)
            time.sleep(0.1)
        except Exception as e:
            pass


if __name__ == '__main__':
    op1 = sys.argv[1]
    urls = sys.argv[2]
    if op1 == '-sub':
        getSubDomain(urls)




