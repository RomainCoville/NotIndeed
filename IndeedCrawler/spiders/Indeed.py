# -*- coding: utf-8 -*-
import scrapy
#import re

class IndeedSpider(scrapy.Spider):
    name = 'Indeed'
    allowed_domains = ['indeed.fr']
    start_urls = ['https://www.indeed.fr/Emplois-data-scientist']

    def parse(self, response):
        # for item in response.css("#SALARY_rbo").css('a'):
        #     print(re.findall("\d+", item.css("::attr(title)").extract_first()))
        #     print(item.css("::attr(title)").extract())

        response.css("#SALARY_rbo").css('a').css("::attr(title)").extract()

        pass
