# -*- coding: utf-8 -*-
import scrapy
import re
from dbmovie.items import DbmovieDetailItem

class DbdetailSpider(scrapy.Spider):
    name = 'dbdetail'
    start_urls = ['https://movie.douban.com/subject/6146955/']

    def parse(self, response):
        detailItem = DbmovieDetailItem()
        content = response.xpath('//*[@id="content"]')

        # 电影详情页的标题
        titles = content.xpath('./h1/span[1]/text()').extract()[0]
        print(titles)
        # 根据空格拆分页面展示的标题 保存到数组中
        titleArray = titles.split(" ")
        # 获取数组的长度 若长度为1 则电影标题只有一节
        titleArrayLength = len(titleArray)
        # 裁剪出中文译名
        title = titleArray[0]

        if(titleArrayLength > 1):
            # 根据空格拆分的标题信息数组不止一节 则为大陆之外地区的电影，获取原始名称
            originalTitle = titles.split(title +  " ")[1]
        else:
            # 标题只有一节 原始标题就是标题
            originalTitle = title
        print(originalTitle)
        detailItem['title'] = title
        detailItem['originalTitle'] = originalTitle

        # 获取电影的年份 带括号
        years = content.xpath('./h1/span[2]/text()').extract()[0]
        # years = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", years) #去掉（）{}[]及其里面的内容
        # 去掉页面展示的年代两端的括号
        years = re.sub(u"\\(|\\)", "", years)
        detailItem['years'] = years
        print(years)
        # 获取id为info的div标签下的所有文本值
        divInfos = response.xpath('//*[@id="info"]/text()').extract()

        infoList = []
        for divInfo in divInfos:
            divInfo = divInfo.strip()
            if divInfo == "":
                # 若list中的值为空 不做处理
                pass
            elif divInfo.startswith("/"):
                # 若list中的值以 /  开头 不做处理
                pass
            else:
                infoList.append(divInfo)

        # for index, value in enumerate(divInfos):
        #     print(index, value)

        # 获取国家和地区
        area = infoList[0]
        print(area)
        # 获取语言
        language = infoList[1]
        print(language)
        # 获取其它片名
        alias = infoList[len(infoList)-1]
        print(alias)

        # 获取导演
        directorArray = content.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        directors = ",".join(directorArray)
        print(directors)

        # 获取编剧
        scenariosStarsSector = content.xpath('//*[@id="info"]/span[2]')
        try:
            # 尝试获取 编剧 标签
            scenarioTag = scenariosStarsSector.xpath('./span[1]/text()').extract()[0]
            if scenarioTag == '编剧':
                # 获取编剧
                scenarioArray = content.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
                scenarios = ",".join(scenarioArray)
                print(scenarios)
            else:
                # 标签的汉字是 编剧
                print("不存在编剧节点")
                scenarios = ""
        except:
            print("没有编剧节点")
            scenarios = ""


        # 获取主演姓名
        starsList = content.xpath('//*[@id="info"]/span[@class="actor"]/span[2]/a/text()').extract()
        starsList = starsList[0:10]
        stars = ",".join(starsList)
        print(stars)

        # 获取电影海报链接
        img = content.xpath('//*[@id="mainpic"]/a/img/@src').extract()[0]
        print(img)

        pass