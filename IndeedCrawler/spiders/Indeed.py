# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import JobCardItem, SalariesItem, JobTypesItem, LocationsItem, CompaniesItem, TitlesItem, StatsItem, JobCards
import re

class IndeedSpider(scrapy.Spider):
    name = 'Job'
    allowed_domains = ['indeed.fr']

    def __init__(self, query='', **kwargs):
        self.start_urls = [f'https://www.indeed.fr/jobs?q={query}&start='] 
        self.query = query
        super().__init__(**kwargs) 

    def parse(self, response):

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

        salaryItem =  SalariesItem(
            salaries = getCategories(salaries),
            salariescount= getCount(salaries)
        )

        jobTypeItem = JobTypesItem(
            jobtypes = getCategories(jobtypes),
            jobtypescount = getCount(jobtypes)
        )

        locationItem = LocationsItem(
            locations = getCategories(locations),
            locationscount = getCount(locations)
        )

        companyItem = CompaniesItem(
            companies = getCategories(companies),
            companiescount = getCount(companies)
        )

        titleItem = TitlesItem(
            titles = getCategories(titles),
            titlescount = getCount(titles)
        )

        yield StatsItem (
            _id = "Stats_" + self.query,
            salaryItem = salaryItem,
            jobTypeItem = jobTypeItem,
            locationItem = locationItem,
            companyItem = companyItem,
            titleItem = titleItem
        )

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

        def clean_spaces(string_):
            if string_ is not None:
                return " ".join(string_.split())

        def cleanJobCard(descriptionList):
            joinedData = ""
            for data in descriptionList:
                joinedData += data
            return clean_spaces(joinedData)
            

        jobCardsList = []
        for job in response.css(".jobsearch-SerpJobCard"):
            title = (job.css(".jobtitle").css("::text").extract())
            company = (job.css(".company").css("::text").extract())
            location = (job.css(".location").css("::text").extract())
            jobCardsList.append(JobCardItem(
                title = cleanJobCard(title),
                company = cleanJobCard(company),
                location = location[0]
            ))

        spiderNumberRegex = "start=(\d)"
        spiderNumber = re.findall(spiderNumberRegex,str(response))[0]

        yield JobCards (
            _id = "JobCards_" + self.query + "_" + spiderNumber,
            jobCardsList = jobCardsList
        )
        
        
