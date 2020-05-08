# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DmoztoolsItem(scrapy.Item):
    category = scrapy.Field()  # Category of the website
    url = scrapy.Field()  # URL of the website
    title = scrapy.Field()  # Title of the website
    description = scrapy.Field()  # Description of the website
    tags = scrapy.Field()  # Tags of the website
