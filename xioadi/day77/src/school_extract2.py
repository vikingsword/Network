import re
import time

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


def getSchool(url):
    with open(r'school2.txt', 'a+', encoding='utf-8') as f:
        for page in range(1, 208):
            soup = getSoup(url + str(page))
            value = soup.find_all('a')
            for item in value:
                if 'list' in item['href']:
                    school_vul = item.text.strip()
                    school = extract_str(school_vul)
                    if school is not None:
                        f.write(school + '\n')
                        print('第' + str(page) + '页:  ' + school)
        f.close()


if __name__ == '__main__':
    url = 'https://src.sjtu.edu.cn/rank/firm/0/?page='
    getSchool(url)
