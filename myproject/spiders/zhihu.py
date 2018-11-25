# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from myproject.items import MyprojectItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['xinhuanet.hifuli.com']
    user_start = 'https://xinhuanet.hifuli.com{user_url}'
    image_start = 'https://www.hiporn.net{image_url}'
    follows_url = 'https://xinhuanet.hifuli.com/chinese?sort=new&page={page}'

    def start_requests(self):
        for page in range(99,8985):
            yield Request(self.follows_url.format(page=page),self.parse_follows)

    def parse_user(self, response):
        #print(response.url)
        image_url = response.xpath('//video/@poster').extract()[0]
        yield {
            'title':response.xpath('//title/text()').extract(),
            'link':response.url,
            'file_urls':response.xpath('//a[@class="btn btn-primary"]/@href').extract(),
            'image_urls':[self.image_start.format(image_url=image_url)],
            }
        
    def parse_follows(self, response):
        #print(response.text)
        #print(response.url)
        user_urls = response.xpath('//a[@target="_self"]/@href').extract()
        for user_url in user_urls:
            yield Request(self.user_start.format(user_url=user_url), self.parse_user)

    def parse(self, response):
        pass
