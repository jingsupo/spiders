# -*- coding: utf-8 -*-
import scrapy


class RobotNewsSpider(scrapy.Spider):
    name = 'robot_news'
    allowed_domains = ['robot-china.com']
    start_urls = ['http://robot-china.com/']

    def parse(self, response):
        pass
