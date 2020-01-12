# -*- coding: utf-8 -*-
import scrapy
from ..items import DemoItem


class Dy2018Spider(scrapy.Spider):
    name = 'dy2018'
    allowed_domains = ['www.dy2018.com']
    start_urls = ['https://www.dy2018.com/html/bikan/']

    def parse(self, response):
        title = response.xpath('//a[@class="ulink"]/text()').extract()[1::2]
        link = response.xpath('//a[@class="ulink"]/@href').extract()[1::2]
        next_page = response.xpath('//div[@class="x"]/a[text()="下一页"]/@href').extract_first()
        for i in range(len(title)-1):
            item = DemoItem()
            item['title'] = title[i]
            item['link'] = 'https://www.dy2018.com' + link[i]
            yield scrapy.Request(url=item['link'], callback=self.parse_url, meta={'item': item})
        if next_page:
            yield scrapy.Request(url='https://www.dy2018.com' + next_page, callback=self.parse)

    def parse_url(self, response):
        down_link = response.xpath('//div[@id="Zoom"]//a/text()').extract_first()
        item = response.meta['item']
        item['down_link'] = down_link
        yield item
