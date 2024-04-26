# !usr/bin/env python
# -*- coding:utf-8 _*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class Demo3Pipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'top250'
        self.ws.append(('标题', '评分', '主题'))

    def open_spider(self):
        pass

    def close_spider(self, spider):
        self.wb.save('movies.xlsx')

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank') or ''
        subject = item.get('subject', '')
        self.ws.append((title, rank, subject))
        return item
