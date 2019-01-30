# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import JobCardItem, SalariesItem, JobTypesItem, LocationsItem, CompaniesItem, TitlesItem
import re

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
            yield JobCardItem(
                title = title,
                company = company,
                location = location
            )


class sideDataSpider(scrapy.Spider):
    name = 'IndeedSideData'
    allowed_domains = ['indeed.fr']
    start_urls = ['https://www.indeed.fr/jobs?q=data+scientist&start=','https://www.indeed.fr/jobs?q=data+analyst&start=','https://www.indeed.fr/jobs?q=data+engineer&start=']

    def parse(self,response):

        def getCategories(category):
            countRegex = "(.*)\s\(\d+\)$"
            categoriescount = []
            print(category)
            for i in range(len(category)):
                categoriescount.append(re.findall(countRegex, category[i])[0])
                categoriescount[i] = categoriescount[i].replace(u'\xa0', u' ')
            return categoriescount

        def getCount(category):
            countRegex = "(\d+)\)$"
            categoriescount = []
            print(category)
            for i in range(len(category)):
                categoriescount.append(re.findall(countRegex, category[i])[0])
            return categoriescount

        salaries = response.css("#SALARY_rbo").css('a').css("::attr(title)").extract()
        jobtypes = response.css("#JOB_TYPE_rbo").css('a').css("::attr(title)").extract()
        locations = response.css("#LOCATION_rbo").css('a').css("::attr(title)").extract()
        companies = response.css("#COMPANY_rbo").css('a').css("::attr(title)").extract()
        titles = response.css("#TITLE_rbo").css('a').css("::attr(title)").extract()

        yield SalariesItem(
            salaries = getCategories(salaries),
            salariescount= getCount(salaries)
        )

        yield JobTypesItem(
            jobtypes = getCategories(jobtypes),
            jobtypescount = getCount(jobtypes)
        )

        yield LocationsItem(
            locations = getCategories(locations),
            locationscount = getCount(locations)
        )

        yield CompaniesItem(
            companies = getCategories(companies),
            companiescount = getCount(companies)
        )

        yield TitlesItem(
            titles = getCategories(titles),
            titlescount = getCount(titles)
        )

    # def clean_spaces(self, string):
    #     if string:
    #         return string.split()
