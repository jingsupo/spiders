# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from .settings import IMAGES_STORE


class MmPipeline(object):
    def process_item(self, item, spider):
        return item


class MmImagesPipeline(ImagesPipeline):
    # 发送每个图片的请求，并自动保存到settings中IMAGES_STORE指定的路径下
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img_src'], meta={'item': item})

    # def item_completed(self, results, item, info):
    #     # 返回图片原来名字的字符串
    #     img_path = IMAGES_STORE + [x['path'] for ok, x in results if ok][0]
    #     img_new_path = IMAGES_STORE
    #     if not os.path.exists(img_new_path):
    #         os.mkdir(img_new_path)
    #     new_name = img_new_path + '/' + item['img_name']
    #     # 更改文件名
    #     try:
    #         os.rename(img_path, new_name)
    #     except Exception as e:
    #         print(e)
    #     return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # path = item['img_name']
        path = '%s/%s' % (item['title'], item['img_name'])
        return path
