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
    # 电影标题 50
    title = scrapy.Field()
    # 电影排名 3
    rank = scrapy.Field()
    # 电影详情页面链接 255
    movieLink = scrapy.Field()
    # 电影评分 4,2
    score = scrapy.Field()
    # 评论人数 10
    commentCount = scrapy.Field()
    # 爬取时间
    scrapyTime = scrapy.Field()
    # 精髓简介 50
    inq = scrapy.Field()

    pass

# 电影详情Item
class DbmovieDetailItem(scrapy.Item):
    # 电影标题
    title = scrapy.Field()
    # 电影年份
    year = scrapy.Field()
    # 其他名称
    otherTile = scrapy.Field()
    # 电影海报链接
    img = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 主演
    starring = scrapy.Field()
    # 电影类型
    category = scrapy.Field()
    # 国家和地区
    area = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 上映日期
    releaseDate = scrapy.Field()
    # 电影时长
    duration = scrapy.Field()
    # 电影其它名称
    alias = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 打分人数
    scoreNum = scrapy.Field()
    # 5星评论比重
    star5 = scrapy.Field()
    # 4星评论比重
    star4 = scrapy.Field()
    # 3星评论比重
    star3 = scrapy.Field()
    # 2星评论比重
    star2 = scrapy.Field()
    # 1星评论比重
    star1 = scrapy.Field()
    # 同类比较
    comparison = scrapy.Field()
    # 评论人数
    commentCount = scrapy.Field()
    # 评论详情页链接地址
    commentLink = scrapy.Field()
    # 问题数量
    questionNum = scrapy.Field()
    # 问题页首页链接
    questionLinking = scrapy.Field()
    # 影评数量
    criticNum = scrapy.Field()
    # 影评页首页链接
    criticLinking = scrapy.Field()

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