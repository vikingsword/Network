import os.path

import requests
from lxml import etree

url = 'https://sc.chinaz.com/jianli/free.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, headers=headers).content

tree = etree.HTML(resp)
resume_link_list = tree.xpath('//div[@id="main"]//p//a/@href')

file_name = 1
if not os.path.exists('result/download'):
    os.mkdir('result/download')
for resume_link in resume_link_list:
    resp2 = requests.get(url=resume_link, headers=headers).content
    tree2 = etree.HTML(resp2)
    download_link_list = tree2.xpath('//div[@id="down"]//ul[@class="clearfix"]/li[1]/a/@href')
    # print(resume_link)
    for download_url in download_link_list:
        resp2 = requests.get(url=download_url, headers=headers).content
        with open('result/download/' + str(file_name) + '.zip', 'wb') as f:
            f.write(resp2)
    print('第 ' + str(file_name) + ' 份简历下载完成！')
    file_name += 1
