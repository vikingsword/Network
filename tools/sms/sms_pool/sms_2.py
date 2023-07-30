import json
from urllib.parse import unquote, parse_qs

import requests

# 无法发送数据包，可能是请求头缺少字段
url = 'https://sytx-login.zshiot.com/Register/PhoneNumber/?handler=GenerateCode'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Cookie': '.AspNetCore.Antiforgery.zbjUl449ekk=CfDJ8HXr7UmmOZxIgrJ1L0JXz7Ad_3ebyoixLifapNwhTS9F9Lyl0SQIXv7ao_ArRuMXrouaUCeGAEK1j9C-56SDGtZd3IdslzwNV8IdhOGkQm2QLLGmTi8i_n29u9pFOHPQYpDx84p-Cn2LrgKAxt3dpi8',
    'RequestVerificationToken': 'CfDJ8HXr7UmmOZxIgrJ1L0JXz7C3rE5iGFjoUmg1GI0uVxax_zkcILrPgAYOObOI2lOR0g57KbDk_o1lbce940KiHwWN7abEe9pY98-kHiFV7BISk_D9C0qLA0apN7epOv-5XQHJV6wfKygnEVdVAxAGQOI'

}
phone_num = input('input your phone number: ')
data = {
    'PhoneNumber': phone_num
}

resp = requests.post(url=url, headers=headers, data=data)

print(resp)
