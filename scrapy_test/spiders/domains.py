import scrapy
import re
from scrapy_test.constant import PATTERN_EMAIL, PATTERN_NUMBER


class DomainsSpider(scrapy.Spider):
    name = "domains"
    allowed_domains = ["example.com"]
    start_urls = ["https://booker-spb.ru/", 'https://frenkelceramics.ru/']

    def parse(self, response):
        email = re.search(PATTERN_EMAIL, response.text)
        number = re.search(PATTERN_NUMBER, response.text)
        return {
                'title': response.css('title::text').get(),
                'description': response.xpath(
                    '//meta[@name="description"]//@content').get(),
                'email': email.group(),
                'number': number.group()
            }