import scrapy

'''
- 基于Spider的全站数据爬取
	- 就是将网站中某板块下的全部页码对应的页面数据进行爬取
	- 需求:爬取校花网中的照片的名称
	- 实现方式:
		-将所有页面的url添加到start_urls列表(不推荐)
		- 自行手动进行请求发送(推荐)
			-手动请求发送:
				- yield scrapy.Request(url,callback):callback专门用做于数据解析
'''


class WallpaperSpider(scrapy.Spider):
    name = "wallpaper"
    start_urls = ["https://www.xxx.com"]

    # url 通用模板
    url = 'xxxx%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('xxx')
        for li in li_list:
            img_name = li.xpaht('xxxxx').extract_first()
            print(img_name)

        if self.page_num <= 11:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动请求发送： callback 回调函数是专门用作于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
