import string, urllib2

def baudu_tieba(url,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        sName = string.zfill(i,5)+'.html'

        print 'downloading page' + str(i) + ',saving as' + sName + '......'
        f=open(sName,'w+')
        m=urllib2.urlopen(url+str(i)).read()
        f.write(m)
        f.close()


bdurl=str(raw_input(u'input=\n'))
begin_page=int(raw_input(u'start\n'))
end_page = int(raw_input(u'end\n'))

baudu_tieba(bdurl,begin_page,end_page)
