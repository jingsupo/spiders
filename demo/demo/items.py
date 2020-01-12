# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    down_link = scrapy.Field()

    source = scrapy.Field()
    crawl_time = scrapy.Field()


class ImgItem(scrapy.Item):
    img_src = scrapy.Field()
