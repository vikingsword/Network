import requests

url = 'https://sytx-login.zshiot.com/Register/PhoneNumber/?handler=GenerateCode'

headers = {
    'Connection': 'close',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'RequestVerificationToken': 'CfDJ8HXr7UmmOZxIgrJ1L0JXz7C3rE5iGFjoUmg1GI0uVxax_zkcILrPgAYOObOI2lOR0g57KbDk_o1lbce940KiHwWN7abEe9pY98-kHiFV7BISk_D9C0qLA0apN7epOv-5XQHJV6wfKygnEVdVAxAGQOI',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://sytx-login.zshiot.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': '.AspNetCore.Antiforgery.zbjUl449ekk=CfDJ8HXr7UmmOZxIgrJ1L0JXz7Ad_3ebyoixLifapNwhTS9F9Lyl0SQIXv7ao_ArRuMXrouaUCeGAEK1j9C-56SDGtZd3IdslzwNV8IdhOGkQm2QLLGmTi8i_n29u9pFOHPQYpDx84p-Cn2LrgKAxt3dpi8',
}

form_data = {
    'PhoneNumber': '+8618845728919',
}

# Send the POST request
response = requests.post(url, headers=headers, data=form_data)

# Process the response
if response.status_code == 200:
    print("POST request successful.")
    print(response.text)
else:
    print("Error occurred during POST request.")
