# -*- coding: utf-8 -*-
import scrapy

class DbmovieSpider(scrapy.Spider):
    name = 'dbmovie'
    start_urls = ['https://movie.douban.com/top250']

    url_set = set()

    def parse(self, response):

        name = response.xpath('//div[@id="wrapper"]/div[@id="content"]/h1/text()').extract()[0]
        print(name)

        movieLi = response.xpath('//*[@id="content"]/div/div[1]/ol/li')

        for li in movieLi:
            title = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            print(title)

