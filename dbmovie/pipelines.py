# -*- coding: utf-8 -*-
# 项目中的pipelines文件
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from dbmovie.items import DbmovieListItem, DbmovieDetailItem, DbmovieCommentItem

class DbmoviePipeline(object):
    def process_item(self, item, spider):

        if isinstance(item, DbmovieListItem):
            # 若为影片列表页的item

            return item
        elif isinstance(item, DbmovieDetailItem):
            # 若为影片详情页的item

            return item
        elif isinstance(item, DbmovieCommentItem):
            # 若为影片评论页的item

            return item
