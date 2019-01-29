# -*- coding: utf-8 -*-
import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'Indeed'
    allowed_domains = ['indeed.fr']
    start_urls = ['https://www.indeed.fr/jobs?q=data+scientist','https://www.indeed.fr/jobs?q=data+analyst','https://www.indeed.fr/jobs?q=data+engineer']

    def parse(self, response):
        for job in response.css(".jobsearch-SerpJobCard"):
            title = (job.css(".jobtitle").css("::text").extract())
            company = (job.css(".company").css("::text").extract())
            location = (job.css(".location").css("::text").extract())
            yield {
                'title' : title,
                'company' : company,
                'location' : location
            }



    # def clean_spaces(self, string):
    #     if string:
    #         return string.split()
