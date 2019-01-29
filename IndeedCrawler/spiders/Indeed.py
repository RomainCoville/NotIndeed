# -*- coding: utf-8 -*-
import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'Indeed'
    allowed_domains = ['indeed.fr']
    start_urls = ['https://www.indeed.fr/jobs?q=data+scientist']

    def parse(self, response):

        # for item in response.css("#SALARY_rbo").css('a'):
        #     print(re.findall("\d+", item.css("::attr(title)").extract_first()))
        #     print(item.css("::attr(title)").extract())

        for job in response.css(".jobsearch-SerpJobCard"):
            title = (job.css(".jobtitle").css("::text").extract())
            company = (job.css(".company").css("::text").extract())
            location = (job.css(".location").css("::text").extract())
            yield {
                'title' : title,
                'company' : company,
                'location' : location
            }
        
        for stats in response.css("#SALARY_rbo").css('a'):
            salary = item.css("::attr(title)").extract()
            yield {
                'salary' : salary
            }

    # def clean_spaces(self, string):
    #     if string:
    #         return string.split()
