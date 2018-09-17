##coding:utf-8
import urllib
import urllib2
import requests
 
 
def get_content_length(data):
    length = len(data.keys()) * 2 - 1
    total = ''.join(list(data.keys()) + list(data.values()))
    length += len(total)
    return length
 
def web_submit(submit_addr,flag,token,success_request,failed_request):
    # 打开Debug Log 方便调试
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)


    try:
        #data是要提交的数据 按照要求的格式填
        data =  {'token': token,'flag': flag,'submit': 'submit'}
        data = urllib.urlencode(data)
        content_length = len(data)
        header = {
            'Host':'172.16.99.129',
            'Content-Type':'application/x-www-form-urlencoded',
            'Origin':'http://172.16.99.129',
            'Accept-Encoding':'gzip, deflate',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
            'Referer':'http://172.16.99.129/flag_submit.php',
            'Content-Length':content_length,
            'Accept-Language':'zh-cn'
        }
        req = urllib2.Request(
                        url = submit_addr,
                        data = data,
                        headers = header
                    )
        response = urllib2.urlopen(req, timeout = 2)
        request_url = response.read()
        #request_url = request_url.decode('gbk')#gbk decode
        if success_request in request_url:
            return {'status':"submit success", 'flag':flag}
        elif failed_request in request_url:
            return {'status':"submit failed", 'flag':flag}
        else:
            return {'status':"submit other", 'flag':flag}
    except urllib2.HTTPError, e:
            return {'status':"submit failed "+ str(e), 'flag':flag}



def main(submit_addr,message,token,success_request,failed_request):
    print message
    flag = message['flag']
    ##submit flag
    #return os.system("echo "+flag)

    ##curl
    #os.system("curl -k 'https://172.16.4.1/Common/awd_sub_answer' -d 'token=35c6f7e1adbbdc0acd8850119c8c0d52&answer='"+flag+" -X POST")

    ##post&&get
    return web_submit(submit_addr,flag,token,success_request,failed_request)




if __name__ == '__main__':
    main(submit_addr,message,token,success_request,failed_request)