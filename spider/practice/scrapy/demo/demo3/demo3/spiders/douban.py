from typing import Iterable

import scrapy
from scrapy import Selector, Request
from pathlib import Path
from ..items import MovieItem
from scrapy.http import HtmlResponse


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    # 一开始直接将url给引擎
    def start_requests(self):
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}&filter=')

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li')
        for list_item in list_items:
            movie = MovieItem()
            movie['title'] = list_item.css('span.title::text').extract_first()
            movie['rank'] = list_item.css('span.rating_num::text').extract_first()
            movie['subject'] = list_item.css('span.inq::text').extract_first()
            # 这里不能返回，而是要使用生成器，将产生的数据交给引擎，引擎再交给管道
            # print('movie')
            yield movie

        # 按照下面的写法或者 def start_request():
        # href_list = sel.css('div.paginator > a::attr(href)')
        # for href in href_list:
        #     url = response.urljoin(href.extract())
        #     yield Request(url)
