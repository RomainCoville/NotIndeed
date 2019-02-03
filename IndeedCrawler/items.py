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
<<<<<<< HEAD
=======

class JobCards(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    _id = scrapy.Field()
    jobCardsList = scrapy.Field()
    pass

class StatsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    _id = scrapy.Field()
    salaryItem = scrapy.Field()
    jobTypeItem = scrapy.Field()
    locationItem = scrapy.Field()
    companyItem = scrapy.Field()
    titleItem = scrapy.Field()
    pass
<<<<<<< HEAD
=======
>>>>>>> c14121d5d5807c8a42ddac6d1bc914481837a2ee
>>>>>>> 605e90ecf1e127f00f0cc9b5179910eb40acf39e
