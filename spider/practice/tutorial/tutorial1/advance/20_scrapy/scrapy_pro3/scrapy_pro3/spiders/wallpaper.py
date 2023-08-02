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
    # allowed_domains = ["www.sss.com"]
    start_urls = ['https://pic.netbian.com/4kmeinv/index_1.html']

    # url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    # page_num = 1

    def parse(self, response):
        # img_name_list = response.xpath('//div[@class="boxgrid"]/a/@title').extract()
        # for img_name in img_name_list:
        #     print(img_name)
        title_list = response.xpath('//div[@class="tui"]//div[@class="title"]/a/text()').extract()
        for title in title_list:
            print(title)
