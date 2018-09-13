#coding:utf-8
import urllib
import urllib2

# 打开Debug Log 方便调试
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)

def main(url):
    try:
        #flag_content = message['flag']
        #data是要提交的数据 按照他要求的格式填
        data =  {u'_xsrf':u'f65fb8fdd4134e1f815c7a10f37561f6',u'place':u'~', u'content':u'asdwqwt', u'time':u'9999/99/99 ab:cd'}
        data = urllib.urlencode(data)
        header = {
            'Accept':'*/*',
            # 'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Cookie':'saeut=CkMPGlSn3wdyh1mEHBWpAg==; user=eGlvbmdiaWFv|1421041643|f368e242dd53c65621ee754688042ae8898c572b;_xsrf=f65fb8fdd4134e1f815c7a10f37561f6',
            'Host':'simpledating.sinaapp.com',
            'Origin':'http://simpledating.sinaapp.com',
            'Referer':'http://simpledating.sinaapp.com/createBroadDating',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0',
            # post要加入的:
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Content-Length':'92',
            'X-Requested-With':'XMLHttpRequest',
        }
        req = urllib2.Request(
                        url = url,
                        data = data,
                        headers = header
                    )
        response = urllib2.urlopen(req)
        print response.read()
    except urllib2.HTTPError, e:
            print 'error', e.code

if __name__ == '__main__':
    main(url)
