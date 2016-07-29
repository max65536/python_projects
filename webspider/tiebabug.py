# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：百度贴吧爬虫
#   版本：0.5
#   作者：lz
#   日期：2016-07-26
#   语言：Python 3.5
#   操作：输入网址后自动只看楼主并保存到本地文件
#   功能：将楼主发布的内容打包txt存储到本地。
#---------------------------------------

import string
import urllib2
import re
'''
class HTML_Tool(object):

    # 用非 贪婪模式 匹配 \t 或者 \n 或者 空格 或者 超链接 或者 图片
    BgnCharToNoneRex=re.compile("(\t|\n| |<a.*?>|<img.*?>)")
    # 用非 贪婪模式 匹配 任意标签
    EndCharToNoneRex=re.compile("<.*?>")

    # 用非 贪婪模式 匹配 任意<p>标签
    BgnPartRex=re.compile("<p.*?>")
    CharToNextTabRex= re.compile("<td>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")

    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]

    def Replace_Char(self,x):
        x=self.BgnCharToNoneRex.sub("",x)
        x=self.BgnPartRex.sub("\n",x)
        x=self.CharToNewLineRex.sub("\n",x)
        x=self.CharToNextTabRex.sub("\t",x)
        x=self.EndCharToNoneRex.sub("",x)

        for t in self.replaceTab:
            x=x.replace(t[0],t[1])
        return x
'''
#----------- 处理页面上的各种标签 -----------
class HTML_Tool:
    # 用非 贪婪模式 匹配 \t 或者 \n 或者 空格 或者 超链接 或者 图片
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")

    # 用非 贪婪模式 匹配 任意<>标签
    EndCharToNoneRex = re.compile("<.*?>")

    # 用非 贪婪模式 匹配 任意<p>标签
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    # 将一些html的符号实体转变为原始符号
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]

    def Replace_Char(self,x):
        x = self.BgnCharToNoneRex.sub("",x)
        x = self.BgnPartRex.sub("\n    ",x)
        x = self.CharToNewLineRex.sub("\n",x)
        x = self.CharToNextTabRex.sub("\t",x)
        x = self.EndCharToNoneRex.sub("",x)

        for t in self.replaceTab:
            x = x.replace(t[0],t[1])
        return x


class Baidu_Spider:
    def __init__(self,url):
        self.myUrl=url+'?see_lz=1'
        self.datas=[]
        self.myTool=HTML_Tool()
        print u'百度贴吧爬虫已启动......'

    # 初始化加载页面并将其转码储存
    def baidu_tieba(self):
        # 读取页面的原始信息并将其从utf-8转码
        Page = urllib2.urlopen(self.myUrl)
        myPage=Page.read().decode("utf-8")
        endPage=self.page_counter(myPage)
        title=self.find_title(myPage)
        print u'文章名称：'+title
        self.save_data(self.myUrl,title,endPage)

    def page_counter(self,myPage):
        myMatch = re.search(r'class="red">(\d+?)</span>', myPage, re.S)
        if myMatch:
            endPage=int(myMatch.group(1))
            print u'共有%d页内容' % endPage
        else:
            endPage=0
            print u'无法计算有多少页内容'
        return endPage

    def find_title(self,myPage):
        myMatch=re.search(r'<h3.*?>(.*?)</h3>',myPage,re.S)
        title=u'无标题'
        if myMatch:
            title=myMatch.group(1)
        else:
            print u'无法获取标题'

        title=title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')
        return title

    def save_data(self,url,title,endPage):
        self.get_data(url,endPage)
        f=open(title+'.txt','w+')
        f.writelines(self.datas)
        f.close()
        print u'文件已下载'
        print u'请按任意键退出'
        raw_input()

    def get_data(self,url,endPage):
        url=url+'&pn='
        for i in range(1,endPage+1):
            print u'爬虫%d号正在加载中...' % i
            myPage=urllib2.urlopen(url+str(i)).read()
            self.deal_data(myPage.decode('utf-8'))

    def deal_data(self,myPage):
        myItems=re.findall('id="post_content.*?>(.*?)</div>',myPage,re.S)
        for item in myItems:
            data=self.myTool.Replace_Char(item.replace("\n","").encode('utf-8'))
            self.datas.append(data+'\n')


print u'请输入贴吧的地址最后的数字串'
bdurl='http://tieba.baidu.com/p/'
tmp=raw_input()
bdurl=bdurl+tmp
mySpider=Baidu_Spider(bdurl)
mySpider.baidu_tieba()



