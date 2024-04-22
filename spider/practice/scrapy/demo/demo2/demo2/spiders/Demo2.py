# !usr/bin/env python
# -*- coding:utf-8 _*-
import scrapy
from pathlib import Path

class QuotesSpider(scrapy.Spider):
    name = 'quotes2'
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)

