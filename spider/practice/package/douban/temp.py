import requests
import xlwt as xlwt
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start=0&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


def create_xlsx():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('douban_top25', cell_overwrite_ok=True)
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '图片')
    sheet.write(0, 2, '排名')
    sheet.write(0, 3, '评分')
    sheet.write(0, 4, '作者')
    sheet.write(0, 5, '简介')
    return book, sheet


def save_to_xlsx(sheet, title, director, img_src, movie_num, rate_num, quote):
    sheet.write(int(movie_num), 0, title)
    sheet.write(int(movie_num), 1, img_src)
    sheet.write(int(movie_num), 2, movie_num)
    sheet.write(int(movie_num), 3, rate_num)
    sheet.write(int(movie_num), 4, director)
    sheet.write(int(movie_num), 5, quote)


def parser_save_movies(movie_soup):
    book, sheet = create_xlsx()
    movies_list = movie_soup.find_all('li')
    for item in movies_list:
        title = None
        director = None
        img_src = None
        movie_num = None
        rate_num = None
        quote = None
        if item.find('img') is not None:
            title = item.find('img').get('alt')
        if item.find('div', attrs={'class', 'bd'}) is not None:
            movie_info = item.find('div', attrs={'class', 'bd'}).find('p').text
            director = str(movie_info).strip().split(' ')[1]
        if item.find('div', attrs={'class', 'pic'}) is not None:
            # 网站上格式是 webp 爬到的是 jpg 且无法打开
            img_src = item.find('div', attrs={'class', 'pic'}).find('img').get('src')
            movie_num = item.find('div', attrs={'class', 'pic'}).find('em').text
            # print(movie_num)
            # print(img_src)y
        if item.find('div', attrs={'class', 'star'}) is not None:
            rate_num = item.find('div', attrs={'class', 'star'}).find('span', attrs={'class', 'rating_num'}).text
            # print(rate_num)
        if item.find('div', attrs={'class', 'bd'}) is not None:
            quote = item.find('div', attrs={'class', 'bd'}).find('p', attrs={'class', 'quote'}).find('span').text
        if title is not None and director is not None and img_src is not None and movie_num is not None and rate_num is not None and quote is not None:
            save_to_xlsx(sheet, title, director, img_src, movie_num, rate_num, quote)
    book.save(u'豆瓣最受欢迎的25部电影.xlsx')

if __name__ == '__main__':
    resp = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    parser_save_movies(soup)