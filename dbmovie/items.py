# -*- coding: utf-8 -*-
# 项目中的item文件
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbmovieItem(scrapy.Item):
    # define the fields for your item here like:
    pass


# 电影排名列表Item
class DbmovieListItem(scrapy.Item):
    # 电影标题
    title = scrapy.Field()
    # 电影排名
    rank = scrapy.Field()
    # 电影详情页面链接
    movieLink = scrapy.Field()
    # 电影评分
    score = scrapy.Field()
    # 评论人数
    commentCount = scrapy.Field()
    # 爬取时间
    scrapyTime = scrapy.Field()
    pass

# 电影详情Item
class DbmovieDetailItem(scrapy.Item):
    # 电影标题
    title = scrapy.Field()
    # 电影年份
    year = scrapy.Field()

    pass

# 评论详情Item
class DbmovieCommentItem(scrapy.Item):
    # 昵称
    nickName = scrapy.Field()
    # 评论星级
    star = scrapy.Field()
    # 评论时间
    commentTime = scrapy.Field()


    pass