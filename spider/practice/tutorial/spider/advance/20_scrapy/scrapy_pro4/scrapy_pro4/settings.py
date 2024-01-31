# Scrapy settings for scrapy_pro4 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_pro4"

SPIDER_MODULES = ["scrapy_pro4.spiders"]
NEWSPIDER_MODULE = "scrapy_pro4.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True
COOKIES = 'lastCity=101050400; wd_guid=15f76cb0-2b91-4972-9c21-91cba73538c7; historyState=state; wt2=Dq1-E0gdVMmYDsHwPXDap2fJY_dGyoN0gZADnn_Jw4vUKMKXKtxsAaGq0FUOPnYZsvaQUmiEaffwjsN6_UXWcZg~~; wbg=0; _bl_uid=tdlIRkwksXqbg1wpe30Ig591bvCm; gdxidpyhxdE=6h2Cu6g0lHNuc%2FKMjsHQyClEsKQ3EYbYiSHA6V091uNA3IPJGW4mVC%2FBPTN6j%2FYLt%5C7dKdW%2BP8BCnpDscTXGK%2Fe3wI0kJ%5COYcg0nBSsXIqzlwuy7%5CBlcTVzsQjfjCKZyYOpYl%2BtzwzY3Rg7EyEafWQNoMDc0nWNNiqy%5C5Q6C0jhgcytO%3A1690897051253; YD00951578218230%3AWM_NI=IjTcgD4w903yA3hWXtPT2y0nbY6apGhNuqwq4hGqNULLl3nKRfESkq7SSLrMO8hQ7aAPHRtJKACdpIEUYzqSNa2oMFLnzEXBuCHEzqGToTO2r6I8Pox2M6MAzDTfKswMYmE%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea6eb3e82eea2afc465f29a8ba3c45f979e9b83c86db8b09d85d43ea2bdba8ac22af0fea7c3b92a8bb69c84e650f8a9f7d1b27383eda8b8db80948cfe9ab366a287fa82f34dac92bb92f67bf8b88992cd5f9094a4d4ed4192ba8bb4ea7bf58d9dadf1478de8a8b2b66b839088b3f742899f8d85f343878b979bf4598ebffe90d04e90b2b6a6db4ab79d88a6f97b858ca1b5ce3ab2ea87d9d365bcee83d7d04bba9c9c87ca79b593978ec837e2a3; YD00951578218230%3AWM_TID=z9tL7slo4DNFQBABUFeQgo8ScQ%2FPcqiC; __zp_seo_uuid__=fdd273d9-3d58-414e-8bdb-3a47135441cb; __l=r=https%3A%2F%2Fwww.google.com%2F&l=%2Fchengshi%2Fc101050400%2F&s=1; __g=-; __zp_stoken__=8798ePF0pDWFJL3s5RmIpQEJDMkAHDmpdZgUpRCd3Ils3DBF%2BaTRtCCkpLkUpI3xsAkcHJEwMBgYhQHoALnpMLgQsQxJtIUohFGhhTwxkR0shIFFSMwR3LSAnVVUebhw1QH41WxcGC35pBXQ%3D; __c=1691028149; __a=22208628.1690896083.1690896083.1691028149.22.2.14.22; geek_zp_token=V1R9skEuT501hsVtRvxhwYKyK47znewSU~'

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_pro4.middlewares.ScrapyPro4SpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_pro4.middlewares.ScrapyPro4DownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_pro4.pipelines.ScrapyPro4Pipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
