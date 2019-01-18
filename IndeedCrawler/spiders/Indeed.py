# -*- coding: utf-8 -*-
import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'Indeed'
    allowed_domains = ['indeed.fr']
    start_urls = ['http://indeed.fr/']

    def parse(self, response):
        pass
