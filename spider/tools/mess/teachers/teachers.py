import requests
from lxml import etree

url = 'https://ss.sut.edu.cn/info/1200/1959.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, headers=headers).content
tree = etree.HTML(resp)
td_list = tree.xpath('//*[@id="vsb_content"]/div//td')
detail_urls = []
for td in td_list:
    try:
        name = td.xpath('./a//text()')[0]
        t_url = td.xpath('./a/@href')[0]
        with open('teachers.txt', 'a+', encoding='utf-8') as f:
            f.write(name + '|' + t_url + '\n')
    except Exception as e:
        pass
