##coding:utf-8
import urllib
import urllib2
import requests
import re


def get_content_length(data):
    length = len(data.keys()) * 2 - 1
    total = ''.join(list(data.keys()) + list(data.values()))
    length += len(total)
    return length


def web_submit(url,flag_start,flag_end):
    # 打开Debug Log 方便调试
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)

    try:
        # data是要提交的数据 按照要求的格式填
        data = {'task_id': "12312321", 'task_content': "123456", 'submit': 'submit'}
        data = urllib.urlencode(data)
        content_length = len(data)
        header = {
            'Host':'172.16.99.129',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding':'gzip, deflate',
            'Referer':'http://172.16.99.129/task_submit.php',
            'Content-Type':'application/x-www-form-urlencoded',
            'Content-Length':content_length,
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',
        }
        req = urllib2.Request(
            url=url,
            data=data,
            headers=header
        )
        response = urllib2.urlopen(req, timeout=2)
        request_url = response.read()
        # request_url = request_url.decode('gbk')#gbk decode
        flag_regex =  r"\b" + flag_start +".*\\" +flag_end
        #judge the flag
        result = re.search(flag_regex, request_url)
        if result:
            flag =result.group()
            return {'getflag_status': "getflag success", 'flag': flag}
        else:
            return {'getflag_status': "getflag failed", 'flag': 'error'}
    except urllib2.HTTPError, e:
        return {'getflag_status': "getflag failed " + str(e), 'flag': 'error'}


def main(url,flag_start,flag_end):
    ##curl
    # os.system("curl -k url -d 'token=35c6f7e1adbbdc0acd8850119c8c0d52&answer='"+flag+" -X POST")

    ##post&&get
    return web_submit(url,flag_start,flag_end)


if __name__ == '__main__':
    main(url,flag_start,flag_end)