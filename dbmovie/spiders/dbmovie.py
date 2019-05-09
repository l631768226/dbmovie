# -*- coding: utf-8 -*-
import scrapy
from dbmovie.items import DbmovieListItem

class DbmovieSpider(scrapy.Spider):
    name = 'dbmovie'
    start_urls = ['https://movie.douban.com/top250']

    url_set = set()

    def parse(self, response):

        base_url = 'https://movie.douban.com/top250'

        name = response.xpath('//div[@id="wrapper"]/div[@id="content"]/h1/text()').extract()[0]
        print(name)

        movieLi = response.xpath('//*[@id="content"]/div/div[1]/ol/li')

        for li in movieLi:
            item = DbmovieListItem()
            # 获取电影排名
            rank = li.xpath('./div/div[1]/em/text()').extract()[0]
            print(rank)
            item['rank'] = rank

            # 获取电影标题
            title = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            print(title)
            item['title'] = title

            # 获取电影平均评分
            score = li.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract()[0]
            print(score)
            item['score'] = score

            # 获取电影的评论人数
            commentCount = li.xpath('./div/div[2]/div[2]/div/span[4]').extract()[0]
            print(commentCount)
            item['commentCount'] = commentCount

            # 电影详情链接
            movieLink = li.xpath('./div/div[2]/div[1]/a/@href').extract()[0]
            print(movieLink)
            item['movieLink'] = movieLink

        try:
            next_url = response.xpath('//*[@id="content"]/div/div[1]/'
                                   'div[2]/span[3]/a/@href').extract()[0]
        except:
            next_url = None
        if next_url is not None:
            next_url = base_url + next_url
            yield response.follow(next_url, callback = self.parse)
        else:
            print("It is over")
