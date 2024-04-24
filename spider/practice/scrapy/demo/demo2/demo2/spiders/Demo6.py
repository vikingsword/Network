# !usr/bin/env python
# -*- coding:utf-8 _*-

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes6"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("span small::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
        yield from response.follow_all(css='ul.pager a', callback=self.parse)