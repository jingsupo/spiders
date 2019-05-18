# -*- coding: utf-8 -*-
import scrapy
from ..items import MmItem


class MeituluSpider(scrapy.Spider):
    name = 'meitulu'
    allowed_domains = ['www.meitulu.com']
    title = ''
    base_url = 'https://www.meitulu.com/item/12235'
    start_urls = [base_url + '.html']

    def parse(self, response):
        page_no = response.xpath('//div[@id="pages"]/span/text()').extract_first()
        img_list = response.xpath('//img[@class="content_img"]/@src').extract()
        for img in img_list:
            item = MmItem()
            item['img_src'] = img
            item['img_name'] = img.split('/')[-1]
            if page_no == '1':
                item['title'] = response.xpath('//h1/text()').extract_first()
                self.title = item['title']
            else:
                item['title'] = self.title
            print(item)
            yield item
        page = 'https://www.meitulu.com' + response.xpath('//div[@id="pages"]/a[text()="下一页"]/@href').extract_first()
        if page:
            yield scrapy.Request(url=page, callback=self.parse)