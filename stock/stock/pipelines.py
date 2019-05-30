# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import json
from pymongo import MongoClient


class StockPipeline(object):
    def process_item(self, item, spider):
        return item


class StockJsonPipeline(object):
    def open_spider(self, spider):
        self.file_name = open('stock.json', 'w', encoding='gbk')

    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + ',\n'
        self.file_name.write(content)
        return item

    def close_spider(self, spider):
        self.file_name.close()


class StockMongoPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient(host='192.168.75.148', port=27017)
        self.db = self.client.stock

    def process_item(self, item, spider):
        self.db.items.insert(dict(item))
        return item
