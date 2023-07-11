import re

import requests
from bs4 import BeautifulSoup


def getSoup(url):
    resp = requests.get(url=url)
    resp.encoding = 'utf-8'
    html = resp.text
    return BeautifulSoup(html, 'html.parser')


def extract_str(str):
    pattern = r'(.*(?:学院|学校|委员会|大学|教育厅))'
    match = re.match(pattern, str)
    if match:
        return match.group(1)
    else:
        return None


url = 'https://src.sjtu.edu.cn/list/?page='

school_set = set()
for page in range(1, 9717):
    url = url + str(page)
    soup = getSoup(url)
    value = soup.find_all('a')
    for item in value:
        if 'post' in item['href']:
            school_vul = item.text.strip()
            school = extract_str(school_vul)
            if school is not None and school not in school_set:
                with open(r'school.txt', 'a+', encoding='utf-8') as f:
                    f.write(school + '\n')
                    school_set.add(school)

