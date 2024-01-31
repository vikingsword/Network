import scrapy

'''
- 图片数据爬取之 ImagesPipeline
    - 基于 scrapy 爬取字符串类型的数据和图片类型的数据的区别：
        - 字符串： 只需要基于 xpath 进行解析且提交管道进行持久化存储
        - 图片： xpath 解析出图片 src 的属性值。单独对图片地址发起请求获取图片的二进制类型的数据
    - ImagesPipeline：
        - 只需要将img的src属性值进行解析，提交到管道，管道就会对图片的src进行请求
            发送获取图片的二进制类型的数据，且还会帮我们进行持久化存储
    - 爬取站长素材中的高清图片
    - 使用流程：
        - 数据解析（图片地址）
        - 将存储 图片地址的item提交到制定的管道类
        - 在管道文件中定制一个基于 ImagesPipeLine 的管道类
            - get_media_request
            - file_path
            - item_completed
        - 在配置文件中
            - 指定图片存储的目录： IMAGES_STORE = './img'
            - 指定开启的管道： 自定制的管道类
        
'''

'''
- 中间件
    - 下载中间件
        - 位置： 引擎和下载器之间
        - 作用： 批量拦截到整个工程中所有的请求和响应
        - 拦截请求：
            - UA 伪装: process_request
            - 代理 IP: process_exception:return request
        - 拦截响应： 
            - 篡改响应数据，响应对象
            - 需求
'''


class ImgSpider(scrapy.Spider):
    name = "img"
    # allowed_domains = ["www.img.com"]
    start_urls = ["https://sc.chinaz.com/tupian/"]

    def parse(self, response):
        # src_list = response.xpath('//div[@class="tupian-list com-img-txt-list masonry"]/div[@class="item masonry-brick"]/img/@src').extract()
        src_list = response.xpath('//div[@class="tupian-list"]').extract()
        for src in src_list:
            print(src)
