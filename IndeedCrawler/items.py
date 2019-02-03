# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobCardItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    pass

class SalariesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    salaries = scrapy.Field()
    salariescount = scrapy.Field()
    pass

class JobTypesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    jobtypes = scrapy.Field()
    jobtypescount = scrapy.Field()
    pass

class LocationsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    locations = scrapy.Field()
    locationscount = scrapy.Field()
    pass

class CompaniesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    companies = scrapy.Field()
    companiescount = scrapy.Field()
    pass

class TitlesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    titles = scrapy.Field()
    titlescount = scrapy.Field()
    pass

class StatsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    _id = scrapy.Field()
    salaryItem = scrapy.Field()
    JobTypeItem = scrapy.Field()
    locationItem = scrapy.Field()
    companyItem = scrapy.Field()
    titleItem = scrapy.Field()
    pass