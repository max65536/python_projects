import urllib2
response=urllib2.uropen('http://www.baidu.com')
html=response.read()
print html