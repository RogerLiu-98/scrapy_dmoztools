# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class DmoztoolsPipeline_toCSV(object):
    def __init__(self):
        columns = ['category', 'url', 'name', 'description', 'tags', 'website_title']
        file_name = 'output.csv'
        self.file = open(file_name, 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, columns)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()
