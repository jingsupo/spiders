#!/usr/bin python
# -*- coding:utf-8 -*-

import requests, time, os
from lxml import etree


class Mmspider(object):
    def __init__(self, base_url, start_page, end_page):
        #self.base_url = "https://www.meitulu.com/item/293"
        #self.base_url = "https://www.meitulu.com/item/8686"
        self.base_url = base_url
        self.offset = 2

        self.headers = {
            # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "Accept-Encoding":"gzip, deflate, br",
            # "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
            # "Cache-Control":"max-age=0",
            # "Connection":"keep-alive",
            # "Host":"www.meitulu.com",
            # "If-None-Match":'W/"5a2db15c-3f32"',
            "Referer":"https://www.meitulu.com/",
            # "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
        }

        self.start = start_page
        self.end = end_page

        self.title = ''

    # 发送请求
    def send_request(self, url, params={}):
        time.sleep(1)
        try:
            response = requests.get(url, params=params, headers=self.headers)
            return response.content
        except Exception as e:
            print (e)

    # 写入文件
    def write_file(self, data, fn):
        print (fn)
        filename = './images/' + self.title + '/' + fn
        with open(filename, 'wb') as f:
            f.write(data)

    # 解析数据
    def parse_data(self, data, xpath):
        # 转换html类型
        html_data = etree.HTML(data)
        # 解析
        data_list = html_data.xpath(xpath)

        return data_list

    # 调度运行
    def run(self):
        start_time = time.time()

        for _ in range(self.start, self.end + 1):
            if self.start == 1:
                url = self.base_url + '.html'
                self.start += 1
                # 发送第一次请求
                first_response = self.send_request(url)
                # 解析获取帖子标题
                self.title = self.parse_data(first_response, '//h1/text()')[0]
                print (self.title)
                # 替换标题中的/，因为目录名称不允许使用/
                self.title = self.title.replace('/', '_')
                if not os.path.exists(self.title):
                    os.mkdir(self.title)
            else:
                url = self.base_url + '_' + str(self.offset) + '.html'
                self.offset += 1
                # 发送第一次请求
                first_response = self.send_request(url)
            # 解析提取子链接 每一条单独的帖子
            first_data_list = self.parse_data(first_response, '//img[@class="content_img"]/@src')
            if not first_data_list:
        	    break
            # 发送图片请求 保存图片到本地
            for img_url in first_data_list:
                # 发送请求
                image_file = self.send_request(img_url)
                # 截取图片链接中的文件名作为要保存的文件名
                fn = img_url.split('/')[-1]
                # 保存图片
                self.write_file(image_file, fn)

        end_time = time.time()

        total_time = end_time - start_time

        print ('总时间%ss' % total_time)


if __name__ == '__main__':
    base_url = "https://www.meitulu.com/item/16718"
    start_page = 1
    end_page = 100

    spider = Mmspider(base_url, start_page, end_page)
    spider.run()
