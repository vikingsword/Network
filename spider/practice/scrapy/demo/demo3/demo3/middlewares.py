# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals, Request

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


def get_cookie_dict():
    cookie_str = 'bid=IYg_Yc51_0w; ll="118123"; _pk_id.100001.4cf6=eea12835099fbdb1.1711375512.; __utma=30149280.190943092.1714144527.1714144527.1714144527.1; __utmz=30149280.1714144527.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1790255367.1714144527.1714144527.1714144527.1; __utmz=223695111.1714144527.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=bb6a0e677db9f546:T=1714144529:RT=1714144529:S=ALNI_MavpqB2rAHND2qeit0KY-czRHh5gQ; __gpi=UID=00000dfc2a97bf99:T=1714144529:RT=1714144529:S=ALNI_MZWy2ugYSHnIfFLckVIprdOw0btKA; __eoi=ID=6d260c7d8999d53f:T=1714144529:RT=1714144529:S=AA-AfjayhjAdx77xljrBAGGlKWhu; FCNEC=%5B%5B%22AKsRol8Gh5d0vP34bgAb3ujaVjdjhBG6-uBDSTLpBmfYWrZMAvb93Cmq4l-dVYG5itHT5I1Zg3Ao2PN94qlazY7l07s-tnoNZUE1ctGhYyoX-PlB3Yyxa6svNW4ovAh5M2-acFZfm9iyW-4_z2ZzB_I7FMNnu2PvYA%3D%3D%22%5D%5D; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1714182635%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; dbcl2="174158182:x+rAvvyYnaU"; ck=aA7H; push_noty_num=0; push_doumail_num=0'
    cookie_dict = {}
    for item in cookie_str.split('; '):
        key, value = item.split('=', maxsplit=1)
        cookie_dict[key] = value
    return cookie_dict


COOKIE_DICT = get_cookie_dict()


class Demo3SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class Demo3DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        # request.meta = {
        #     'proxy': 'socks5://127.0.0.1:10808'
        # }

        # 拦截器，给请求添加cookie或代理信息，配置后可用 DOWNLOADER_MIDDLEWARES
        request.cookies = COOKIE_DICT
        # return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
