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
    # 电影标题 var 14
    title = scrapy.Field()
    # 电影排名 int 3
    rank = scrapy.Field()
    # 电影详情页面链接 var 50
    movieLink = scrapy.Field()
    # 电影评分 double 4,2
    score = scrapy.Field()
    # 评论人数 int 10
    commentCount = scrapy.Field()
    # 爬取时间 timestamp
    scrapyTime = scrapy.Field()
    # 精髓简介 var 50
    inq = scrapy.Field()

    pass

# 电影详情Item
class DbmovieDetailItem(scrapy.Item):
    # 电影标题 var 14
    title = scrapy.Field()
    # 原始标题 var 50
    originalTitle = scrapy.Field()
    # 电影年份 var 4
    years = scrapy.Field()
    # 其他名称 var 100
    otherTiles = scrapy.Field()
    # 电影海报链接 var 100
    img = scrapy.Field()
    # 导演 var 20
    directors = scrapy.Field()
    # 编剧 var 30
    scenarios = scrapy.Field()
    # 主演 var 255
    starring = scrapy.Field()
    # 电影类型 var 20
    category = scrapy.Field()
    # 国家和地区 var 20
    area = scrapy.Field()
    # 语言  var 30
    language = scrapy.Field()
    # 上映日期 var 70
    releaseDate = scrapy.Field()
    # 电影时长  var 6 待议
    duration = scrapy.Field()
    # 电影其它名称 var 70
    alias = scrapy.Field()
    # 评分 double 3,1
    score = scrapy.Field()
    # 打分人数 int 9
    scoreNum = scrapy.Field()
    # 5星评论比重 double 3,1
    star5 = scrapy.Field()
    # 4星评论比重 double 3,1
    star4 = scrapy.Field()
    # 3星评论比重 double 3,1
    star3 = scrapy.Field()
    # 2星评论比重 double 3,1
    star2 = scrapy.Field()
    # 1星评论比重 double 3,1
    star1 = scrapy.Field()
    # 同类比较  var 30
    comparison = scrapy.Field()
    # 评论人数 int 9
    commentCount = scrapy.Field()
    # 评论详情页链接地址 var 50
    commentLink = scrapy.Field()

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
    rating = scrapy.Field()
    # 评论时间
    commentTime = scrapy.Field()
    # 评论内容
    short = scrapy.Field()
    # 获取有用数量
    vote = scrapy.Field()

    pass