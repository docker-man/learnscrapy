# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MyprojectItem

class HifuliSpider(scrapy.Spider):
    name = 'hifuli'
    allowed_domains = ['hifuli.com']
    start_urls = ['https://xinhuanet.hifuli.com/chinese?sort=new&page=1']

    def parse(self, response):
        titles = response.xpath('//h3/text()').extract()
        for title in titles:
            yield {
                'title':title.strip(),
                'url':response.url,
            }

        urls = response.xpath('//a/@href').extract()
        for url in urls:
            yield response.follow(url, callback=self.parse)