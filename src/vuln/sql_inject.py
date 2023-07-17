import requests
from bs4 import BeautifulSoup

cookie = 'OTZ=7080741_24_24__24_; HSID=AF4HgCLTHauT_KnFh; SSID=AEfBKPjiHOvtHmFf9; APISID=OlNGvJaiamu7jKvO/ANCy3fVS5LzpoPlh4; SAPISID=iJvyXNtPjANsr4Oe/App0Sa9XFJVMr1gvd; __Secure-1PAPISID=iJvyXNtPjANsr4Oe/App0Sa9XFJVMr1gvd; __Secure-3PAPISID=iJvyXNtPjANsr4Oe/App0Sa9XFJVMr1gvd; SEARCH_SAMESITE=CgQI35gB; SID=YwjyBQQP1jnmf3SdohAbKmg7WdfmwnxotREtN54XIpymlMI26G-gEfaJ14bMTb4eoJ6OJg.; __Secure-1PSID=YwjyBQQP1jnmf3SdohAbKmg7WdfmwnxotREtN54XIpymlMI2ZcCyuj0aIXTAnyoxRNAmLQ.; __Secure-3PSID=YwjyBQQP1jnmf3SdohAbKmg7WdfmwnxotREtN54XIpymlMI2lYo5GdRF0ztofPBzmJ4sJA.; AEC=Ad49MVG50QXKcXYV4EZCR3LO-VF1RW5ECHfMHcU-Cx9rtYI_l8-cU9t4YgU; NID=511=ROcqRCPcP8S3_uq1x-U1ImbwS2eJ91rrUAfi7jHM0Bwt_pmhTm9c4jVGrihgUjFwHRfikmaV2cT1sweOSEOAQj6VjZIGa9QofIVzMO5BexARsLflLWMxLlA_ut9sj31eI4RWMLCCkc2BPKUEIl31x6bK60m9gywu9bvI45XkJdMGSXBgDAQ1kbPBrdiSbDhLZL8F7ByojlsmTobYMHv8fXZOak5LqXT3-x6rQ8MLYk0XEPA5E8d5nZMP244MIs1N5PCjRIgIo_kPguyP90taLeqWzI9InamQwuSlrPNG-H_ZVDVuNLgt0de9BkgiSbde2H7-WA; GOOGLE_ABUSE_EXEMPTION=ID=54ed54cd1b4dd1ed:TM=1689592596:C=r:IP=38.59.243.90-:S=waV2JU5BRNUEb9Ou5BNppSk; DV=M-svhfeq-YJTUFfdruUpeWrVsd47llgvJBy_9Krq5AQAABBY3CpeACv-1gEAAHxNq3cj6LfMeAAAAAd64O4hw7ADIgAAAA; 1P_JAR=2023-07-17-12; __Secure-1PSIDTS=sidts-CjEBPu3jIbb1Fj0VQEq5QT7-R533xLBkOxOygpY42tvxWqR0OzgXDranUam5cdwS-KxsEAA; __Secure-3PSIDTS=sidts-CjEBPu3jIbb1Fj0VQEq5QT7-R533xLBkOxOygpY42tvxWqR0OzgXDranUam5cdwS-KxsEAA; SIDCC=APoG2W_RNzdr1PXT9yTfJHMqDBo3_cwX-itjeDHlkzLFGNqwtyMaWWfWnsPdjjFfiAbCtdEUuV8; __Secure-1PSIDCC=APoG2W-kAmn9NNaTIXU5_I40VVeBK5nm5j8miiZaSpoPlnaoLHNEaj2YA2DRTGfuotJLpSrEdAw; __Secure-3PSIDCC=APoG2W_pJ5QMNZZ4kmnU9BzNsro0dn5eRRQI2Km45CaVrDo0Iv861BpQG_5chKBkxvnR88PyBQ'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie': cookie
}

proxies = {
    'http': 'http://127.0.0.1:10808'
}

# 输入搜索内容 例如 inurl:asp?id=1 学校/公司/学院/医院
search_content = 'inurl:asp?id=1'

key_list = ['学校', '公司', '大学', '学院', '医院', '中学']

for key in key_list:
    for page in range(0, 300, 10):

        google_search_url = 'https://www.google.com/search?q=' + search_content + '%20' + str(key) + '&start=' + str(page)
        resp = requests.get(url=google_search_url, headers=headers, proxies=proxies)

        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            url_list = soup.find_all('cite', attrs={'class', 'apx8Vc qLRx3b tjvcx GvPZzd cHaqb'})
            count = 1

            for url in url_list:

                target = str(url.text).replace(' ', '').replace('›', '/')
                modified_url = target.rsplit('/', 1)[0] + '?' + target.rsplit('/', 1)[1]

                if count % 2 == 1:
                    with open('sql_inject.txt', 'a+', encoding='utf-8') as f:
                        f.write(modified_url + '\n')

                count += 1

        else:
            print('error')

