import scrapy
import json
import time

class MangoSpiderSpider(scrapy.Spider):


    name = 'mango_spider'
    start_urls = [
        'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99'
    ]

    def parse(self, response):
        title = response.css('.product-name').extract()
        price = response.css('.product-sale--discount').extract()
        color = response.css('.colors-info-name').extract()
        size = response.xpath('//select[@id="selector-list"]/option/text()').getall()

        scraped_info = {
            'title': title,
            'price': price,
            'color': color,
            'size': size
        }
        f = open('data.json', 'w')
        json.dump(scraped_info, f, indent=4)
        f.close()

