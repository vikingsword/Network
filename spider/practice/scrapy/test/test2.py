# !usr/bin/env python
# -*- coding:utf-8 _*-
import scrapy

class crawl(spider.Spider):
    name = "quotes"
    start_url = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "author": quote.xpath('span/small/text()').get(),
                "text": quote.css('span.text::text').get(),
            }

        page_next = response.css('li.text a::attr("href")').get()
        if page_next is not None:
            yield response.follow(self, page_next)
