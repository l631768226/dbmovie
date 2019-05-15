# -*- coding: utf-8 -*-
import scrapy

class DbdetailSpider(scrapy.Spider):
    name = 'hsc'
    # start_urls = ['https://www.zhihu.com/question/297715922']
    start_urls = ['https://www.zhihu.com/question/46435597']

    def parse(self, response):
        # 获取包含问题的节点
        content = response.xpath('//*[@id="QuestionAnswers-answers"]'
                                 '/div[@class="Card AnswersNavWrapper"]'
                                 '/div[@class="ListShortcut"]'
                                 '/div[@class="List"]')

        if content is not None:
            # 若节点不为空则继续获取
            # 获取每一条答案的节点
            answersList = content.xpath('//div[@class="List-item"]')
            print(len(answersList))
            for answersItem in answersList:
                contentItem = answersItem.xpath('./div[@class="ContentItem AnswerItem"]')
                itemId = contentItem.xpath('./@name').extract()[0]
                print(itemId)

        else:
            # 若节点为空 则结束
            print('问题节点为空')
            pass

        pass