# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class IndeedSpider(scrapy.Spider):
    name = 'Indeed'
    allowed_domains = ['indeed.fr']
    start_urls = ['https://www.indeed.fr/jobs?q=data+scientist&start=','https://www.indeed.fr/jobs?q=data+analyst&start=','https://www.indeed.fr/jobs?q=data+engineer&start=']

    def parse(self, response):
        i = 0
        all_links = []
        for i in range(10):
            j = i*10
            all_links.append(str(response).split(" ")[1][:-1] + str(j))

        for link in all_links :
            yield Request(link, callback=self.parse_category)

    def parse_category(self, response):

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


class sideDataSpider(scrapy.Spider):
    name = 'IndeedSideData'
    allowed_domains = ['indeed.fr']
    start_urls = ['https://www.indeed.fr/jobs?q=data+scientist&start=','https://www.indeed.fr/jobs?q=data+analyst&start=','https://www.indeed.fr/jobs?q=data+engineer&start=']

    def parse(self,response):
        for salaries in response.css("#SALARY_rbo").css('a'):
            salary = salaries.css("::attr(title)").extract()
            yield {
                'salary' : salary
            }

        for jobs in response.css("#JOB_TYPE_rbo").css('a'):
            jobtype = jobs.css("::attr(title)").extract()
            yield {
                'jobtype' : jobtype
            }

        for locations in response.css("#LOCATION_rbo").css('a'):
            location = locations.css("::attr(title)").extract()
            yield {
                'location' : location
            }

        for companies in response.css("#COMPANY_rbo").css('a'):
            company = companies.css("::attr(title)").extract()
            yield {
                'company' : company
            }

        for titles in response.css("#TITLE_rbo").css('a'):
            title = titles.css("::attr(title)").extract()
            yield {
                'title' : title
            }



    # def clean_spaces(self, string):
    #     if string:
    #         return string.split()
