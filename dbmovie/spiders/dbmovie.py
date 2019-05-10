# -*- coding: utf-8 -*-
import scrapy

from dbmovie.items import DbmovieListItem
from dbmovie.items import DbmovieDetailItem
from dbmovie.items import DbmovieCommentItem

class DbmovieSpider(scrapy.Spider):
    name = 'dbmovie'
    start_urls = ['https://movie.douban.com/top250']

    url_set = set()

    def parse(self, response):

        base_url = 'https://movie.douban.com/top250'

        name = response.xpath('//div[@id="wrapper"]/div[@id="content"]/h1/text()').extract()[0]
        print(name)
        # 获取包含电影信息的标签列表
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

            yield scrapy.Request(item['movieLink'],
                                 callback= self.parse_detail)
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


    def parse_detail(self, response):

        detailItem = DbmovieDetailItem()
        content = response.xpath('//*[@id="content"]')
        # 电影详情页标题
        title = content.xpath('./h1/span[1]/text()').extract()[0]
        print(title)
        detailItem['title'] = title

        commentLink = response.xpath('//*[@id="comments-section"]'
                                     '/div[1]/h2/span/a/@href').extract()[0]
        print(commentLink)

        yield scrapy.Request(commentLink, callback = self.parse_comment)


    def parse_comment(self, response):
        # 接收电影详情页传递的参数
        url = response.request.url
        baseUrl = url.split("?")[0]
        commentItem = DbmovieCommentItem()
        commentDivs = response.xpath('//*[@id="comments"]/div[@class="comment-item"]')
        for commentDiv in commentDivs:
            # 获取评论人员的昵称
            nickName = commentDiv.xpath('./div[2]/h3/span[2]/a/text()').extract()[0]
            print(nickName)

            try:
                # 获取下一页的地址链接（需要拼接）
                next_url = response.xpath('//*[@id="paginator"]/a[@class="next"]/@href').extract()[0]
            except:
                next_url = None

            if next_url is not None:
                # 组拼下一页评论详情的连接地址
                next_url = baseUrl + next_url
                yield response.follow(next_url, callback=self.parse_comment)
            else:
                print("these comments are over")