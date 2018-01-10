# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from robot_china.items import RobotChinaItem, DetailItem
from datetime import datetime
from scrapy.exporters import CsvItemExporter
import json
from pymongo import MongoClient


class RobotChinaPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, RobotChinaItem):
            item['crawl_time'] = str(datetime.utcnow())
            item['source'] = spider.name

        return item


class RobotChinaCsvPipeline(object):
    def open_spider(self, spider):
        self.file_name_list = open('robot_china_list.csv', 'w')
        self.file_name_page = open('robot_china_page.csv', 'w')
        # 创建csv文件读写对象，参数为需要读写的文件对象
        self.csv_exporter_list = CsvItemExporter(self.file_name_list)
        self.csv_exporter_page = CsvItemExporter(self.file_name_page)
        # 开始执行读写操作
        self.csv_exporter_list.start_exporting()
        self.csv_exporter_page.start_exporting()

    def process_item(self, item, spider):
        if isinstance(item, RobotChinaItem):
            self.csv_exporter_list.export_item(item)
        if isinstance(item, DetailItem):
            self.csv_exporter_page.export_item(item)

        return item

    def close_spider(self, spider):
        self.csv_exporter_list.finish_exporting()
        self.csv_exporter_page.finish_exporting()
        self.file_name_list.close()
        self.file_name_page.close()


class RobotChinaJsonPipeline(object):
    def open_spider(self, spider):
        self.file_name_list = open('robot_china_list.json', 'w')
        self.file_name_page = open('robot_china_page.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, RobotChinaItem):
            self.file_name_list.write(json.dumps(dict(item)) + ',\n')
        if isinstance(item, DetailItem):
            self.file_name_page.write(json.dumps(dict(item)) + ',\n')

        return item

    def close_spider(self, spider):
        self.file_name_list.close()
        self.file_name_page.close()


class RobotChinaMongodbPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client.robot_china

    def process_item(self, item, spider):
        self.db.items.insert(dict(item))
