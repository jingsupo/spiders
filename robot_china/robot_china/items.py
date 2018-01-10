# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RobotChinaItem(scrapy.Item):
    """
        列表页item
    """
    # 文章标题
    title = scrapy.Field()
    # 文章链接
    link = scrapy.Field()

    # 抓取时间
    crawl_time = scrapy.Field()
    # 爬虫源
    source = scrapy.Field()


class DetailItem(scrapy.Item):
    """
        详情页item
    """
    # 发布时间
    publish_time = scrapy.Field()
    # 文章出处
    publish_from = scrapy.Field()
    # 文章内容
    publish_data = scrapy.Field()
