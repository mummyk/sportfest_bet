import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Breakingbet(scrapy.Spider):
    name = "Bbet"

    def start_requests(self):
        url = 'https://breaking-bet.com/en/prematch'
        # wait for the page to load or for an element to load
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=10,
                              wait_until=EC.element_to_be_clickable((By.CLASS_NAME, 'percent')))

    def parse(self, response):
        profit = response.css('.profit span::text').get()
        yield {'profit': profit}
