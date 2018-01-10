# -*- coding: utf-8 -*-
import scrapy
from robot_china.items import RobotChinaItem, DetailItem


class RobotNewsSpider(scrapy.Spider):
    # 爬虫名字
    name = 'robot_news'
    # 运行爬取的域名
    allowed_domains = ['robot-china.com']

    base_url = 'http://www.robot-china.com/news/list-937'
    # 将所有url放入start_urls，实现真正高并发
    start_urls = [base_url + '.html'] + [base_url + '-' + str(num) + '.html' for num in range(2, 1396 + 1)]

    def parse(self, response):
        page_list = response.xpath('//div[@id="tab"]/ul')
        for page in page_list:
            item = RobotChinaItem()
            item['title'] = page.xpath('.//h2/span/a/text()').extract_first()
            item['link'] = page.xpath('.//h2/span/a/@href').extract_first()

            # 发送详情页请求，并指定回调函数
            yield scrapy.Request(url=item['link'], callback=self.parse_detail)
            # 每获取一条信息就将item提交给引擎，然后转交给管道处理
            yield item

    def parse_detail(self, response):
        item = DetailItem()
        item['publish_time'] = ''.join(response.xpath('//div[@class="zx3"]//li[2]/text()').extract())
        item['publish_from'] = ''.join(response.xpath('//div[@class="zx3"]//li[3]/text()').extract())
        item['publish_data'] = ''.join(response.xpath('//div[@class="content"]/div/text()').extract())

        yield item
