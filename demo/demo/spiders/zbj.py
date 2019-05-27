# -*- coding: utf-8 -*-
import scrapy
from ..items import ZBJItem


class ZbjSpider(scrapy.Spider):
    name = 'zbj'
    allowed_domains = ['zbj.com']
    base_url = 'https://task.zbj.com/t-dashujufuwu/page'
    offset = 1
    start_urls = [base_url + str(offset) + '.html']

    def parse(self, response):
        title = response.xpath('//div[@class="demand"]//p[@class="d-title"]/span/@title').extract()
        link = response.xpath('//div[@class="demand"]/a/@href').extract()
        price = response.xpath('//div[@class="demand"]//p[@class="d-base"]/b/text()').extract()
        participants = response.xpath('//div[@class="demand"]//p[@class="d-base"]/span[2]/text()').extract()
        print('*'*50)
        print(len(title), len(link), len(price), len(participants))
        print('*'*50)
        for i in range(len(title)-1):
            item = ZBJItem()
            item['title'] = title[i]
            item['link'] = link[i]
            item['price'] = price[i]
            # item['participants'] = participants[i]  # 此字段条数和其他字段不一致，导致保存出错
            yield item
        self.offset += 1
        if self.offset <= 36:
            page = self.base_url + str(self.offset) + '.html'
            if page:
                yield scrapy.Request(url=page, callback=self.parse)
