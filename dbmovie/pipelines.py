# -*- coding: utf-8 -*-
# 项目中的pipelines文件
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from dbmovie.items import DbmovieListItem, DbmovieDetailItem, DbmovieCommentItem

class DbmoviePipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='dbmovie',
            user='root',
            passwd='ly10',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()


    def process_item(self, item, spider):

        if isinstance(item, DbmovieListItem):
            # 若为影片列表页的item
            self.cursor.execute(
                """insert into movieItem (title, rank, movieLink, score, commentCount, scrapyTime, inq, img) 
                values(%s, %s, %s, %s, %s, %s, %s, %s)""",
                (item['title'], item['rank'], item['movieLink'], item['score'],
                 item['commentCount'], item['scrapyTime'], item['inq'], item['img']))
            self.connect.commit()
            return item
        elif isinstance(item, DbmovieDetailItem):
            # 若为影片详情页的item
            self.cursor.execute(
                """insert into movieDetail (
                title, originalTitle, years, img, directors, rank,
                scenarios, starring, category, area, lang, releaseDate, 
                duration, alias, score, scoreNum, star5, star4, 
                star3, star2, star1, comparison, commentCount, commentLink
                ) 
                values(
                %s, %s, %s, %s, %s, %s,  
                %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s
                )""",
                (item['title'], item['originalTitle'], item['years'], item['img'], item['directors'], item['rank'],
                item['scenarios'], item['starring'], item['category'], item['area'], item['lang'], item['releaseDate'],
                item['duration'], item['alias'], item['score'], item['scoreNum'], item['star5'], item['star4'],
                item['star3'], item['star2'], item['star1'], item['comparison'], item['commentCount'], item['commentLink']
                ))
            self.connect.commit()
            return item
        elif isinstance(item, DbmovieCommentItem):
            # 若为影片评论页的item

            return item
