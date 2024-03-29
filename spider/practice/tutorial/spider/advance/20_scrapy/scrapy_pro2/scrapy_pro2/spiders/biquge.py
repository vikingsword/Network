import scrapy
from ..items import ScrapyPro2Item

'''
- scrapy 持久化存储
    - 基于终端指令(不推荐)：
        - 要求： 只可以将 parse 方法的返回值存储到本地的文本文件中
        - 注意： 持久化存储对应的文本文件类型只可以是('json', 'jsonlines', 'jsonl', 'jl', 'csv', 'xml', 'marshal', 'pickle')
        - 指令： scrapy crawl -o ./xxx.csv
    - 基于管道(推荐):
        - 编码流程：
            - 数据解析
            - 在item类中定义相关的属性
            - 将解析的数据封装存储到item类型的对象
            - 将item类型的对象提交给管道进行持久化存储的操作
            - 在管道类的process_item中要将其接受到的item对象中存储的数据进行持久化存储操作
            - 在配置文件中开启管道
        - 好处：
            - 通用性强
- 面试题:将爬取到的数据一份存储到本地一份存储到数据库,如何实现?
    - 管道文件中一个管道类对应的是将数据存储到一种平台
    - 爬虫文件提交的item只会给管道文件中第一个被执行的管道类接受
    - process_item中的return item表示将item传递给下一个即将被执行的管道类
'''


class BiqugeSpider(scrapy.Spider):
    name = "biquge"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ['https://www.biquge7.xyz/ph']

    # 基于终端指令
    # def parse(self, response):
    #     # extract() 将selector对象或者selector列表中的data对象提取出来; extract_first() 提取列表中第 0 个列表元素
    #     title_list = response.xpath('//div[@class="tui"]//div[@class="title"]/a/text()').extract()
    #     for title in title_list:
    #         print(title)
    #     return ''.join(title_list)

    # 基于管道
    def parse(self, response):
        # extract() 将selector对象或者selector列表中的data对象提取出来; extract_first() 提取列表中第 0 个列表元素
        title_list = response.xpath('//div[@class="tui"]//div[@class="title"]/a/text()').extract()
        for title in title_list:
            item = ScrapyPro2Item()
            item['title'] = title
            # 将 item 提交给管道
            yield item
