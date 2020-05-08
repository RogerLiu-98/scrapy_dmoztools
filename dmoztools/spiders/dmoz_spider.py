import scrapy
from dmoztools.items import DmoztoolsItem


class DmozToolsSpider(scrapy.Spider):
    name = 'dmoztools_spider'

    def __init__(self, category='', *args, **kwargs):
        super(DmozToolsSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ["dmoztools.net"]
        # If we don't set category, then the crawler will begin at http://dmoztools.net/,
        # else it will begein at the category we set
        self.category = category
        self.start_urls = ["http://dmoztools.net/%s" % self.category]

    def parse(self, response):
        if self.category is '':
            # Parse all categories on the main page
            all_categories_hrefs = response.xpath('//*[@id="category-section"]//aside/div/h2/a/@href').extract()
            for href in all_categories_hrefs:
                url = response.urljoin(href)
                yield scrapy.Request(url, callback=self.parse_category_content)
        else:
            # Parse all subcategories on this site
            all_href = response.xpath('//*[@id="subcategories-section"]//div[@class="cat-item"]//@href').extract()
            for href in all_href:
                url = response.urljoin(href)
                yield scrapy.Request(url, callback=self.parse_category_content)

    def parse_category_content(self, response):
        sites_xpath = response.xpath('//*[@id="site-list-content"]//div[@class="site-item "]//div['
                                     '@class="title-and-desc"]')
        # Find the category, url, title, description and tags
        if sites_xpath:
            tags = ';'.join(response.url.split('/')[3:-1])
            for site in sites_xpath:
                item = DmoztoolsItem()
                item['category'] = self.category
                item['url'] = site.xpath('a/@href').extract()[0].strip()
                item['title'] = site.xpath('a/div/text()').extract()[0].strip()
                item['description'] = site.xpath('div/text()').extract()[0].strip()
                item['tags'] = tags
                yield item

        categories_xpath = response.xpath('//*[@id="subcategories-section"]//div[@class="cat-item"]//@href')
        if categories_xpath:
            all_href = categories_xpath.extract()
            for href in all_href:
                url = response.urljoin(href)
                yield scrapy.Request(url, callback=self.parse_category_content)