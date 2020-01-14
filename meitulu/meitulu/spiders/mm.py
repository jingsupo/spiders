# -*- coding: utf-8 -*-
import scrapy
from ..items import MeituluItem


class MmSpider(scrapy.Spider):
    name = 'mm'
    allowed_domains = ['www.meitulu.com']
    start_urls = ['https://www.meitulu.com/item/16362.html']

    def parse(self, response):
        img_list = response.xpath('//img[@class="content_img"]/@src').extract()
        for img in img_list:
            item = MeituluItem()
            item['img_src'] = img
            item['img_name'] = img.split('/')[-1]
            item['title'] = response.xpath('//title/text()').extract_first().split('_')[0]
            yield item
        next_page = response.xpath('//div[@id="pages"]/a[text()="下一页"]/@href').extract_first()
        if next_page:
            yield scrapy.Request(url='https://www.meitulu.com'+next_page, callback=self.parse)
