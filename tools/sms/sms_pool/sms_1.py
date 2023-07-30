import requests

phone_num = input('input your phone number: ')
url = 'http://boyunkong.cn:18081/captcha/captchaForPhone?phoneNumber=' + phone_num
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

resp = requests.get(url=url, headers=headers)

res = resp.json()

print(res['msg'])

