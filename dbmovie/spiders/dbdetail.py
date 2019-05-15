# -*- coding: utf-8 -*-
import scrapy
import re
from dbmovie.items import DbmovieDetailItem

class DbdetailSpider(scrapy.Spider):
    name = 'dbdetail'
    start_urls = ['https://movie.douban.com/subject/1292722/']

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
        print(title)
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
        detailItem['years'] = years

        # 获取id为info的div标签下的所有文本值
        divInfos = response.xpath('//*[@id="info"]/text()').extract()

        infoList = []
        for divInfo in divInfos:
            divInfo = divInfo.strip()
            if divInfo == "":
                # 若list中的值为空 不做处理
                pass
            elif divInfo.startswith("/") & ("分" not in divInfo) :
                # 若list中的值以 /  开头 不做处理
                pass
            else:
                infoList.append(divInfo)

        # for index, value in enumerate(divInfos):
        #     print(index, value)

        # 获取国家和地区
        area = infoList[0]
        print(area)
        detailItem['area'] = area

        # 获取语言
        language = infoList[1]
        print(language)
        detailItem['language'] = language

        # 获取其它片名
        alias = infoList[len(infoList)-1]
        print(alias)
        detailItem['alias'] = alias

        # 获取导演
        directorArray = content.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        directors = ",".join(directorArray)
        print(directors)
        detailItem['directors'] = directors

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
        detailItem['scenarios'] = scenarios

        # 获取主演姓名
        starsList = content.xpath('//*[@id="info"]/span[@class="actor"]/span[2]/a/text()').extract()
        starsList = starsList[0:10]
        starring = ",".join(starsList)
        print(starring)
        detailItem['starring'] = starring

        # 获取电影海报链接
        img = content.xpath('//*[@id="mainpic"]/a/img/@src').extract()[0]
        print(img)
        detailItem['img'] = img

        # 获取影片时长
        try:
            duration = content.xpath('//*[@id="info"]/span[@property="v:runtime"]/text()').extract()[0]
        except:
            duration = infoList[2]
        print(duration)
        detailItem['duration'] = duration

        # 获取上映日期
        releaseDateArray= content.xpath('//*[@id="info"]/'
                                        'span[@property="v:initialReleaseDate"]/'
                                        'text()').extract()
        releaseDate = ",".join(releaseDateArray)
        print(releaseDate)
        detailItem['releaseDate'] = releaseDate

        # 获取影片类型
        categoryArray = content.xpath('//*[@id="info"]/span[@property="v:genre"]/'
                                      'text()').extract()
        category = ",".join(categoryArray)
        print(category)
        detailItem['category'] = category

        # 获取电影评分
        score = content.xpath('//strong[@class="ll rating_num"]/text()').extract()[0]
        print(score)
        detailItem['score'] = score

        # 获取评分人数
        scoreNum = content.xpath('//span[@property="v:votes"]/text()').extract()[0]
        print(scoreNum)
        detailItem['scoreNum'] = scoreNum

        # 获取星级评价比重
        ratingWeightArray = content.xpath('//span[@class="rating_per"]/text()').extract()
        star5 = ratingWeightArray[0].replace("%", "")
        star4 = ratingWeightArray[1].replace("%", "")
        star3 = ratingWeightArray[2].replace("%", "")
        star2 = ratingWeightArray[3].replace("%", "")
        star1 = ratingWeightArray[4].replace("%", "")
        print(star5, star4, star3, star2, star1)
        detailItem['star5'] = star5
        detailItem['star4'] = star4
        detailItem['star3'] = star3
        detailItem['star2'] = star2
        detailItem['star1'] = star1

        # 获取同类比较信息
        ratingBetterArray = content.xpath('//div[@class="rating_betterthan"]'
                                          '/a/text()').extract()
        comparison = ','.join(ratingBetterArray)
        print(comparison)
        detailItem['comparison'] = comparison

        # 获取短评数量
        commentCount = response.xpath('//*[@id="comments-section"]'
                                     '/div[1]/h2/span/a/text()').extract()[0]
        commentCountArray = commentCount.split(" ")
        commentCount = commentCountArray[1]
        print(commentCount)
        detailItem['commentCount'] = commentCount

        # 获取短评列表链接地址
        commentLink = response.xpath('//*[@id="comments-section"]'
                                     '/div[1]/h2/span/a/@href').extract()[0]
        print(commentLink)
        detailItem['commentLink'] = commentLink

        pass