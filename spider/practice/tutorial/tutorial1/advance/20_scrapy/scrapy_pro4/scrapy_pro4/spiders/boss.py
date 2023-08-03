import scrapy
'''
    - 请求传参: 
        - 使用场景： 如何爬取解析的数据不在同一张页面中。（深度爬取）
        - 需求：爬取 boss 的岗位名称， 岗位描述
'''

class BossSpider(scrapy.Spider):
    name = "boss"
    # allowed_domains = ["www.sss.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=python&city=101070100"]

    def parse(self, response):
        li_list = response.xpath('//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]')
        for li in li_list:
            title = li.xpath('//span[@class="job-name"]/text()').extract()
            print(title)
