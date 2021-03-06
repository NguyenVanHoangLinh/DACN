# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class Products_Item(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_old_price = scrapy.Field()
    product_link = scrapy.Field()
    category_name = scrapy.Field()
    product_site = scrapy.Field()
    product_image = scrapy.Field()
    