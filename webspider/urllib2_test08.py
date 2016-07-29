from urllib2 import Request,urlopen,URLError,HTTPError

old_url='http://rrurl.cn/b1UZuP'
req = Request(old_url)
response= urlopen(req)
print 'old url:'+old_url
print 'real url:'+response.geturl()
print 'Info():'
print response.info()
