import scrapy


class WallpaperSpider(scrapy.Spider):
    name = "wallpaper"
    # allowed_domains = ["www.sss.com"]
    start_urls = ["https://wall.alphacoders.com/popular.php?page=1"]
    url = 'https://wall.alphacoders.com/popular.php?page=%d'
    page_num = 1

    def parse(self, response):
        img_name_list = response.xpath('//div[@class="boxgrid"]/a/picture/img/@alt')
        for img_name in img_name_list:
            print(img_name)

