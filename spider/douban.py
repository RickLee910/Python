# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/2 0:56
import re  # 正则表达式，文字匹配
import urllib as ur# 指定 URL，获取网页数据
from bs4 import BeautifulSoup  # 网页解析
import xlwt  # 进行excel操作
import urllib.request
import urllib.error
def main():
    baseurl = 'https://movie.douban.com/top250?start='

    datalist = getdata(baseurl)
    savepath = ".\\豆瓣电影TOP250.xls"
    #savedata(savepath)
    askURL(baseurl)
# 1.爬网页
def getdata(baseurl):
    datalist = []
    for i in range(10):          #调用获取页面信息函数10次
        url = baseurl + str(i*25)
        html = askURL(url)
        # 2.逐一解析数据



    return datalist

def askURL(url):
    #模拟浏览器偷不信息，向豆瓣服务器发送信息
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
    request = ur.request.Request(url,headers=head)
    html = ""
    try:
        response = ur.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except ur.error.HTTPError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html


# 3.保存数据
def savedata(savepath):
    pass

if __name__ == "__main__":
