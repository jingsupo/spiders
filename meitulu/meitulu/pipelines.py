# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
from scrapy.pipelines.images import ImagesPipeline


class MeituluPipeline(object):
    def process_item(self, item, spider):
        return item


class MeituluImagesPipeline(ImagesPipeline):
    # 发送每个图片的请求，并自动保存到settings中IMAGES_STORE指定的路径下
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img_src'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # path = item['img_name']
        path = '%s/%s' % (item['title'], item['img_name'])
        return path
