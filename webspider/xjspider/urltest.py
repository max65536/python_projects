# -*- coding: utf-8 -*-
import cookielib
import gzip
import urllib
import urllib2

import re


def ungzip(data):
    try:
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data
def getOpener(head):
    # deal with the Cookies
    cj = cookielib.CookieJar()
 #   pro = urllib.request.HTTPCookieProcessor(cj)
  #  opener = urllib.request.build_opener(pro)
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

url='http://www.zhihu.com/'

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
 #   'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}

opener=getOpener(header)

data=opener.open(url)
#data=ungzip(data)
#print data.read()

_xsrf=getXSRF(data.read())
print _xsrf

url+='login/email'
id='lzslqs@163.com'
psd='lll1995911'

postdict={
    '_xsrf':_xsrf,
    'email':id,
    'password':psd,
    'remember_me':'true',
    'captcha_type':'cn'
}

postdata=urllib.urlencode(postdict).encode()
data=opener.open(url,postdata).read()
#data=ungzip(data)

print data

data=opener.open('http://www.zhihu.com/')

print data.read()






