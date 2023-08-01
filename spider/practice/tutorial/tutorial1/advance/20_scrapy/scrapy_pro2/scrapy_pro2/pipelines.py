# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyPro2Pipeline:
    fp = None

    def open_spider(self, spider):
        print('开始爬虫....')
        self.fp = open('./demo.txt', 'w', encoding='utf-8')

    # 每次接收到一个 item 就会被调用一次
    def process_item(self, item, spider):
        title = item['title']
        self.fp.write(title + '\n')
        # return 了就会将 item 传给下一个即将执行的管道类，建议要 return
        return item

    def close_spider(self, spider):
        print('结束爬虫....')
        self.fp.close()


# 管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class mysqlPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', db='python',
                                    charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into books (name) values("%s")' % (item["title"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
