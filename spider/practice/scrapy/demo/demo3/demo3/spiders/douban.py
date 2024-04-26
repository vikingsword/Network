import scrapy
from scrapy import Selector
from pathlib import Path
from ..items import MovieItem
from scrapy.http import HtmlResponse

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response:HtmlResponse):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li')
        for list_item in list_items:
            movie = MovieItem()
            movie['title'] = list_item.css('span.title::text').get()
            movie['rank'] = list_item.css('span.rating_num::text').get()
            movie['subject'] = list_item.css('span.inq::text').get()
            # 这里不能返回，而是要使用生成器，将产生的数据交给引擎，引擎再交给管道
            print('movie')
            yield movie

        href_list = sel.css('div.pageinator > a::attr("href")')
        for href in href_list:
            url = response.urljoin(href.extract())
            print('url = ', url)
