import requests
from bs4 import BeautifulSoup

url = 'https://src.sjtu.edu.cn/rank/firm/0/?page='
count = 0
for page in range(1, 205):
    pageUrl = url + str(page)
    res = requests.get(url=pageUrl)
    soup = BeautifulSoup(res.text, 'html.parser')
    # linkList = soup.find('td', attrs={'class', 'am-text-center'}).find_all('a')
    linkList = soup.find('table', attrs={'class', 'am-table minos-list am-text-sm am-table-bordered am-table-hover am-scrollable-horizontal'}).find_all('a')
    for i in linkList:
        count += 1
        print(i.text)
        with open('school_name.txt', 'a+') as f:
            f.write(i.text + '\n')
f.close()
print(count)
