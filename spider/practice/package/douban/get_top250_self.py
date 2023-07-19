import requests
import xlwt
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start='

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


def parser_save_movies():
    book, sheet = create_xlsx()
    for page in range(0, 250, 25):
        target = url + str(page)
        resp = requests.get(url=target, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')
        movies_list = soup.find_all('li')
        for item in movies_list:
            if item.find('div', attrs={'class', 'item'}) is not None:
                title = item.find('img').get('alt')

                movie_info = item.find('div', attrs={'class', 'bd'}).find('p').text

                director = str(movie_info).strip().split(' ')[1]

                # 网站上格式是 webp 爬到的是 jpg 且无法打开
                img_src = item.find('div', attrs={'class', 'pic'}).find('img').get('src')

                movie_num = item.find('div', attrs={'class', 'pic'}).find('em').text

                rate_num = item.find('div', attrs={'class', 'star'}).find('span', attrs={'class', 'rating_num'}).text

                quote = None
                if item.find('span', attrs={'class', 'inq'}) is not None:
                    quote = item.find('span', attrs={'class', 'inq'}).text

                save_to_xlsx(sheet, title, director, img_src, movie_num, rate_num, quote)
    book.save(u'豆瓣最受欢迎的250部电影2.xlsx')


if __name__ == '__main__':
    parser_save_movies()
