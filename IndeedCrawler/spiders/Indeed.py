# -*- coding: utf-8 -*-
import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'Indeed'
    allowed_domains = ['indeed.fr']
    start_urls = ['https://www.indeed.fr/jobs?q=data+scientist','https://www.indeed.fr/jobs?q=data+analyst','https://www.indeed.fr/jobs?q=data+engineer']

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
