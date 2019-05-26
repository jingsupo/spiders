# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    amount = scrapy.Field()
    detail_attr = scrapy.Field()

    source = scrapy.Field()
    crawl_time = scrapy.Field()


class ImgItem(scrapy.Item):
    img_src = scrapy.Field()
