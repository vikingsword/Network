import requests as requests
from whois import whois

# website = 'https://whois.chinaz.com/'
# target = input('input your url: ')
# url = website + target
# res = requests.get(url)
# print(res.content)
# data = whois.get('www.xiaodi8.com')
# print(data)
data2 = whois('www.xiaodi8.com')
print(data2)

