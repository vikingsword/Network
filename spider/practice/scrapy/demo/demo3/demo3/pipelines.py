# !usr/bin/env python
# -*- coding:utf-8 _*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
import pymysql

class DbPipeline:

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306,
                                    user='root', passwd='123456',
                                    database='spider', charset='utf8mb4')
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        if len(self.data) > 0:
            self._execute()
        self.conn.close()

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', 0.0)
        subject = item.get('subject', '')
        duration = item.get('duration', 0)
        intro = item.get('intro', '')
        self.data.append((title, rank, subject, duration, intro))
        if len(self.data) == 100:
            self._execute()
            self.data.clear()
        return item

    def _execute(self):
        self.cursor.executemany(
            'insert into top_movie (`title`, `rank`, `subject`, `duration`, `intro`) values (%s, %s, %s, %s, %s)',
            self.data
        )
        self.conn.commit()


class ExcelPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'top250'
        self.ws.append(('标题', '评分', '主题', '时长', '简介'))

    # def open_spider(self):
    #     pass

    def close_spider(self, spider):
        self.wb.save('movies.xlsx')

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', 0.0)
        subject = item.get('subject', '')
        duration = item.get('duration', 0)
        intro = item.get('intro', '')
        self.ws.append((title, rank, subject, duration, intro))
        return item
