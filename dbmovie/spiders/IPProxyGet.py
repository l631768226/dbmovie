# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree  #导入html树形结构转换模块

def GetIP():
    ips = []
    url = 'https://www.kuaidaili.com/free'
    r = urllib.request.urlopen(url).read().decode("utf-8",'ignore')
    r = etree.HTML(r)
    IpTr = r.xpath('//*[@id="list"]/table/tbody/tr')

    for ipTr in IpTr:
        ip = ipTr.xpath('./td[@data-title = "IP"]/text()')
        print(ip)
        port = ipTr.xpath('./td[@data-title="PORT"]/text()')
        print(port)
        ips.append("http://" + ip[0] + ":" + port[0])

    return ips
# def GetIP():
#     url = 'https://www.xicidaili.com/'
#     # url = 'https://www.kuaidaili.com/free'
#     r = urllib.request.urlopen(url).read().decode("utf-8", 'ignore')
#     r = etree.HTML(r)
#     oddTr = r.xpath('//*[@id="ip_list"]/tbody/tr[@class = "odd"]')
#     for tr in oddTr:
#         ip = tr.xpath("./td[2]/text()").extract()[0]
#         port = tr.xpath("./td[3]/text()").extract()[0]
#         type = tr.xpath("./td[6]/text()").extract()[0]
#         print(ip)
#         print(port)
#         print(type)