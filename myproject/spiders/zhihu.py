# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from myproject.items import MyprojectItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['xinhuanet.hifuli.com']
    #start_urls = ['http://www.zhihu.com/']
    user_start = 'https://xinhuanet.hifuli.com{user_url}'
    follows_url = 'https://xinhuanet.hifuli.com/chinese?sort=new&page={page}'

    def start_requests(self):
        for page in range(1,10):
            yield Request(self.follows_url.format(page=page),self.parse_follows)

    #def start_requests(self):
    #    #yield Request(self.user_url, self.parse_user)
    #    yield Request(self.follows_url,self.parse_follows)

    def parse_user(self, response):
        print(response.url)
        yield {
            'title':response.xpath('//title/text()').extract(),
            'url':response.url,
            'desc':response.xpath('//video/source/@src').extract(),
            }
        
    def parse_follows(self, response):
        #print(response.text)
        #print(response.url)
        user_urls = response.xpath('//a[@target="_self"]/@href').extract()
        for user_url in user_urls:
            yield Request(self.user_start.format(user_url=user_url), self.parse_user)

    def parse(self, response):
        pass
