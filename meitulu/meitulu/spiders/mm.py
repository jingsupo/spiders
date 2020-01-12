# -*- coding: utf-8 -*-
import scrapy
from ..items import MeituluItem


class MmSpider(scrapy.Spider):
    name = 'mm'
    allowed_domains = ['www.meitulu.com']
    start_urls = ['https://www.meitulu.com/item/1025.html']  # [Bomb.TV] 逢泽莉娜 Rina Aizawa 2011-01
    # start_urls = ['https://www.meitulu.com/item/4817.html']  # [YS Web] vol.671 安枝瞳 - 《濡れた瞳》 写真套图
    # start_urls = ['https://www.meitulu.com/item/4092.html']  # [YS Web] Vol.635 菜乃花 Nanoka 写真集
    # start_urls = ['https://www.meitulu.com/item/3985.html']  # [@misty] No.247 – 爱田樱(あいださくら Sakura Aida) 写真套图
    # start_urls = ['https://www.meitulu.com/item/19185.html']  # [YS-Web] Vol.824 菜乃花 Nanoka
    # start_urls = ['https://www.meitulu.com/item/13191.html']  # [Wanibooks] #162 橋本梨菜 Rina Hashimoto 写真套图
    title = ''

    def parse(self, response):
        page_no = response.xpath('//div[@id="pages"]/span/text()').extract_first()
        img_list = response.xpath('//img[@class="content_img"]/@src').extract()
        for img in img_list:
            item = MeituluItem()
            item['img_src'] = img
            item['img_name'] = img.split('/')[-1]
            if page_no == '1':
                item['title'] = response.xpath('//h1/text()').extract_first()
                self.title = item['title']
            else:
                item['title'] = self.title
            yield item
        page = 'https://www.meitulu.com' + response.xpath('//div[@id="pages"]/a[text()="下一页"]/@href').extract_first()
        if page:
            yield scrapy.Request(url=page, callback=self.parse)
