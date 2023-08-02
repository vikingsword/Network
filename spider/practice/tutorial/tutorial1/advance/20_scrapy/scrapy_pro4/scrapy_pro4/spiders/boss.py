import scrapy


class BossSpider(scrapy.Spider):
    name = "boss"
    allowed_domains = ["www.sss.com"]
    start_urls = ["https://www.sss.com"]

    def parse(self, response):
        pass
