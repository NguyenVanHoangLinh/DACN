# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
class TutorialPipeline(object):
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '123' # your password
        database = 'discount'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into categories(name) select %(category_name)s where not exists(select name from categories where name = %(category_name)s)",item)
        self.cur.execute("insert into website(site) select %(product_site)s where not exists(select site from website where site = %(product_site)s)",item)
        self.cur.execute("insert into discount(product_name,product_price,product_old_price,product_link,category_name,product_site,product_image) values(%(product_name)s,%(product_price)s,%(product_old_price)s,%(product_link)s,%(category_name)s,%(product_site)s,%(product_image)s)",item)
        self.connection.commit()
        return item
    
