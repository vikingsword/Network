import scrapy

'''
scrapy框架的基本使用
    - 环境的安装：
        - mac or linux: pip install scrapy
        - windows(python >= 3.8)
            - pip install scrapy
        - windows(python < 3.8):
            - pip install wheel
            - 下载twisted，下载地址为 http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
            — 安装twisted： pip install Twisted—17.1.0—cp36—cp36m—win_amd64.whl
            - pip install pywin32
            - pip install scrapy
            测试：在终端里录入scrapy指令，没有报错即表示安装成功！
    - 创建一个工程： scrapy startproject xxxPro
    - cd xxxPro
    - 在spiders子目录中创建一个爬虫文件
        - scrapy genspider spiderName www.xxx.com
    - 执行工程：
        - scrapy crawl spiderName
'''


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称：就是爬虫源文件的一个唯一标识
    name = "first"
    # 允许的域名：用来限定start＿urls列表中哪些url可以进行请求发送
    # allowed_domains = ["www.baidu.com"]
    # 起始的url列表：该列表中存放的url会被scrapy息动进行请求的发送
    start_urls = ["https://www.baidu.com", "https://sogou.com"]

    # 用作于数据解析：response参数表示的就是请求成功后对应的响应对象
    def parse(self, response):
        print(response)
