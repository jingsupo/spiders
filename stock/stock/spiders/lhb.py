# -*- coding: utf-8 -*-
import scrapy
import json


class LhbSpider(scrapy.Spider):
    name = 'lhb'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=200,'
                  'page=1,sortRule=-1,sortType=,startDate=2019-05-30,endDate=2019-05-30,gpfw=0,'
                  'js=var%20data_tab_1.html?rt=25987511']

    def parse(self, response):
        data = json.loads(response.text.split('=', 1)[1])['data']
        for item in data:
            yield item
