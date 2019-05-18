# -*- coding: utf-8 -*-
import scrapy
from ..items import MmItem


class MeituluSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['www.meizitu.com']
    # base_url = 'https://www.meizitu.com/a/5521'
    base_url = 'http://www.meizitu.com/a/5399'
    start_urls = [base_url + '.html']

    def parse(self, response):
        img_list = response.xpath('//div[@id="picture"]//img/@src').extract()
        for img in img_list:
            item = MmItem()
            item['title'] = response.xpath('//div[@class="metaRight"]/h2/a/text()').extract_first()
            item['img_src'] = img
            item['img_name'] = img.split('/')[-1]
            print(item)
            yield item
