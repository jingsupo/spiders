# -*- coding: utf-8 -*-
import scrapy
from ..items import DemoItem, ImgItem


class A1688Spider(scrapy.Spider):
    name = '1688'
    allowed_domains = ['1688.com', 'alicdn.com']
    start_urls = ['https://detail.1688.com/offer/536255690440.html']

    def parse(self, response):
        title = response.xpath('//h1[@class="d-title"]/text()').extract_first()
        price = response.xpath('//tr[@class="price"]//span[@class="value price-length-4"]/text()').extract()
        amount = response.xpath('//tr[@class="amount"]//span[@class="value"]/text()').extract()
        de_feature = response.xpath('//div[@id="mod-detail-attributes"]//td[@class="de-feature"]/text()').extract()
        de_value = response.xpath('//div[@id="mod-detail-attributes"]//td[@class="de-value"]/text()').extract()
        img_url = response.xpath('//div[@id="mod-detail-description"]//div[@id="desc-lazyload-container"]/@data-tfs-url').extract_first()
        item = DemoItem()
        item['title'] = title
        item['price'] = price
        item['amount'] = amount
        item['detail_attr'] = dict(zip(de_feature, de_value))
        yield scrapy.Request(url=img_url, callback=self.parse_img)
        yield item

    def parse_img(self, response):
        img_src = response.xpath('//img/@src').extract()
        for img in img_src:
            item = ImgItem()
            item['img_src'] = img.split('\\')[1].split('"')[1]
            yield item
