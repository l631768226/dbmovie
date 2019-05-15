#coding=utf-8

from scrapy import cmdline

# name = 'dbmovie'
# name = 'dbdetail'
name = 'commentdetail'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())