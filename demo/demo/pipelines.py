# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from .items import DemoItem, ImgItem
import json
from pymongo import MongoClient
from datetime import datetime


class DemoPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, DemoItem):
            item['source'] = spider.name
            item['crawl_time'] = str(datetime.utcnow())
        return item


class DemoJsonPipeline(object):
    def open_spider(self, spider):
        self.file_name = open('demo.json', 'w', encoding='gbk')

    def process_item(self, item, spider):
        if isinstance(item, DemoItem):
            content = json.dumps(dict(item)) + ',\n'
            self.file_name.write(content)
        return item

    def close_spider(self, spider):
        self.file_name.close()


class DemoMongoPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient(host='192.168.75.50', port=27017)
        self.db = self.client.demo

    def process_item(self, item, spider):
        if isinstance(item, DemoItem):
            self.db.items.insert(dict(item))
        return item


class ImgPipeline(ImagesPipeline):
    # 发送每个图片的请求，并自动保存到settings中IMAGES_STORE指定的路径下
    def get_media_requests(self, item, info):
        if isinstance(item, ImgItem):
            yield scrapy.Request(url=item['img_src'], meta={'item': item})

    # def file_path(self, request, response=None, info=None):
    #     item = request.meta['item']
    #     # path = item['img_name']
    #     path = '%s/%s' % (item['title'], item['img_name'])
    #     return path
