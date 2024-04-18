#this file is where we're telling Scrapy where to look the exact data it wants to look for, this is specific to each webpage we wish to scrape.

from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

#a class that inherits Stackspider from spider and required attributes are added.
class StackSpider(Spider):
    name="stack"             #defines the name of the spider
    allowed_domains=["stackoverflow.com"]          #base-url for allowed domains
    start_urls=["http://stackoverflow.com/questions?pagesize=50&sort=newest"]          #exact URLs for the spider to crawl.

    def parse(self,response):
        # Log the response URL for debugging
        self.logger.info(f"Scraping URL: {response.url}")

        # Extract questions using the updated XPath        
        questions= Selector(response).xpath('//div[@class="s-post-summary--content"]')

        # Check if any questions are found
        if not questions:
            self.logger.warning("No questions found!")

        

        for question in questions:
            item= StackItem()
            item["title"]=question.xpath('.//h3/a[@class="s-link"]/text()').extract_first()    #idhar we are assigning values by iterating through questions and assigning the "title" and "url"
            item["url"] = question.xpath('.//h3/a[@class="s-link"]/@href').extract_first()
            yield item                          #yeild keyword is used to return a list of values from a function

