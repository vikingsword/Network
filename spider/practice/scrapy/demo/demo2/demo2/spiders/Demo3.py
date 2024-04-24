# !usr/bin/env python
# -*- coding:utf-8 _*-

import scrapy
from pathlib import Path


class QuotesSpider(scrapy.Spider):
    name = "quotes3"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
            page = response.url.split('/')[-2]
            filename = f'info-{page}.html'
            Path(filename).write_bytes(response.body)
