import requests
import xlwt as xlwt
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
count = 0
book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '图片')
sheet.write(0, 2, '排名')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '作者')
sheet.write(0, 5, '简介')
for page in range(0, 250, 25):
    url = 'https://movie.douban.com/top250?start=' + str(page)
    # print(url)
    resp = None
    try:
        resp = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(resp.content, 'html.parser')

        ol_list = soup.find('ol', attrs={'class', 'grid_view'}).find_all('li')
        for item in ol_list:
            item_name = item.find('span', attrs={'class', 'title'}).text
            img_link = item.find(class_='pic').find('a').find('img')['src']
            item_img = item.find('a').find('img').get('src')
            item_index = item.find(class_='').string
            item_score = item.find(class_='rating_num').string
            item_author = item.find('p').text
            item_intr = item.find(class_='inq').string
            # print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)
            # print(img_link)
            sheet.write(int(item_index), 0, item_name)
            sheet.write(int(item_index), 1, item_img)
            sheet.write(int(item_index), 2, item_index)
            sheet.write(int(item_index), 3, item_score)
            sheet.write(int(item_index), 4, item_author)
            sheet.write(int(item_index), 5, item_intr)
    except Exception as e:
        pass
book.save(u'豆瓣最受欢迎的250部电影.xlsx')


print(count)

# res = requests.get(url='https://movie.douban.com/top250?start=150', headers=headers)
# print(res.text)
