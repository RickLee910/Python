# -*- coding: utf-8 -*-
# __author__:song
# 2020/12/2 8:38
import urllib.request
import urllib.parse
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8')) #对获取到的网页源码进行utf-8解码

#获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen(("http://httpbin.org/post"),data = data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#     print(response.read().decode("utf-8"))
# except:
#     print("time out!")

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheaders())
#例子
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({'name':'eruc'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

#伪装成浏览器访问网址
url = "https://douban.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))