# -*- coding: utf-8 -*-
import scrapy

from dbmovie.items import DbmovieCommentItem

class DbdetailSpider(scrapy.Spider):
    name = 'commentdetail'
    start_urls = ['https://movie.douban.com/subject/1292722/comments?status=P']

    def parse(self, response):

        cDiv = response.xpath('//div[@class="comment"]')
        print(len(cDiv))

        for comment in cDiv:
            # 获取 有用 数量
            vote = comment.xpath('./h3/span[1]/span[1]/text()').extract()[0]
            print(vote)
            DbmovieCommentItem['vote'] = vote

            commentInfo = comment.xpath('./h3/span[@class = "comment-info"]')

            # 评论人员的昵称
            nickName = commentInfo.xpath('./a/text()').extract()[0]
            print(nickName)
            DbmovieCommentItem['nickName'] = nickName

            # 获取 星级评论等级
            rating = commentInfo.xpath('./span[2]/@title').extract()[0]
            print(rating)
            DbmovieCommentItem['rating'] = rating

            # 获取评论时间
            commentTime = commentInfo.xpath('./span[3]/text()').extract()[0].strip()
            print(commentTime)
            DbmovieCommentItem['commentTime'] = commentTime

            # 获取评论内容
            short = comment.xpath('./p/span[@class = "short"]/text()').extract()[0]
            print(short)
            DbmovieCommentItem['short'] = short