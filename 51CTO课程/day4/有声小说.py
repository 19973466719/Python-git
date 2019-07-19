
import requests
import request
class Spider(object):
    def start_request(self):
        response=requests.get("https://www.qidian.com/all")
        print(response.txt)
#1.请求一级页面，拿到HTLM源代码，抽取小说名，小说链接  创建文件夹
#2.请求二级页面，拿到HTLM源代码， 抽取章名，章链接
#3.请求三级页面拿到HTML源代码，抽取文章内容，保存内容
spider=Spider()
spider.start_request()