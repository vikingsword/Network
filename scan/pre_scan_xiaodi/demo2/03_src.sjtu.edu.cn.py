import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
target = 'https://src.sjtu.edu.cn/list/?page='
# https://src.sjtu.edu.cn/list/?page=2
collegeList = []

for page in range(1, 100):
    url = target + str(page)
    print(url)
    res = requests.get(url=url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    linkList = soup.find_all('a')

    try:
        for i in linkList:
            content = i.text.strip()
            if content.__contains__('大学') or content.__contains__('教育厅') or content.__contains__('学院') or content.__contains__('学校'):
                content = content[:content.index('存在')]
                collegeList.append(content)
    except Exception as e:
        pass

collegeList = list(set(collegeList))
for i in collegeList:
    with open(r'college.txt', 'a', encoding='utf-8') as f:
        f.write(i + '\n')
        f.close()
