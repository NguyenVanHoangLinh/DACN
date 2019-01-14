import scrapy
from ..items import Products_Item
from scrapy.utils.markup import remove_tags
class RealEstateSpider(scrapy.Spider):
    name = "sendo"
    start_urls = ['https://www.sendo.vn/khuyen-mai/']

    def parse(self, response):
        # follow links to sendo page
        for href in response.css('div.overflow_box a::attr(href)'):
            yield response.follow(href, self.parse_sendo)

        # follow pagination links
        next_page_url = response.css('div.pagination li:nth-child(8) a::attr(href)').extract_first()
        if next_page_url is not None:
            next_page_url=response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url,callback=self.parse)

    def parse_sendo(self, response):
        def extract_with_css(query):
            try:
                result = response.css(query).extract_first().strip()
            except:
                result = ""
            return result
        product_name = extract_with_css('h1.productName_Dx2F::text')
        product_price = extract_with_css('strong.currentPrice_1aHy::text')
        product_old_price = extract_with_css('span.oldPrice_2xa_::text')
        product_link = '' + response.request.url
        category_name = extract_with_css('ol.breadcrumb_PQxo li:nth-child(2) a::text')
        product_site = 'sendo'
        product_img = extract_with_css('figure.imageSquare_3d75 img::attr(src)')
        product_image = product_img[2:]
        productItem = Products_Item(product_name=product_name,product_price=product_price,product_old_price=product_old_price,product_link=product_link,category_name=category_name,product_site=product_site,product_image=product_image)
        yield productItem