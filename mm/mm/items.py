# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题作为保存图片的文件夹名
    title = scrapy.Field()
    # 图片链接
    img_src = scrapy.Field()
    # 图片名字
    img_name = scrapy.Field()
