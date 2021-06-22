##coding:utf-8
import os
import requests
import subprocess
import sys


def requests_submit(submit_addr,token,success_request,failed_request,message):

    try:

        flag = message['flag']

        formdata = {"token":token,"flag":flag,}
        headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        cookies = {"cookie_name": "cookie_value", }
        response = requests.post(submit_addr, data = formdata, headers = headers, cookies=cookies, verify = False, timeout=3)
        # print(response.text)

        if success_request in response.text:
            message['submit_status'] ="submit success"
            return message
        elif failed_request in response.text:
            message['submit_status'] ="submit failed"
            return message
        else:
            message['submit_status'] ="submit other reasons"
            return message
    except Exception, e:
        message['submit_status'] = "submit failed:"+ str(e)
        return flag

def curl_submit(submit_addr,token,success_request,failed_request,message):
    try:
        flag = message['flag']
        ##curl -s slient -k no vertify -X POST -d data
        curl_order = "curl -s -k -X POST {0} -d 'token={1}&flag={2}'".format(submit_addr,token,flag)
        response = subprocess.check_output(curl_order, shell=True)
        if success_request in response:
            message['submit_status'] ="submit success"
            return message
        elif failed_request in response:
            message['submit_status'] ="submit failed"
            return message
        else:
            message['submit_status'] ="submit other reasons"
            return message
    except Exception, e:
        message['submit_status'] = "submit failed:"+ str(e)
        return message


def main(submit,message):
    if submit.submit_method == "curl":
        return curl_submit(submit.submit_addr,submit.token,submit.success_request,submit.failed_request,message)

    elif submit.submit_method == "requests":
        return requests_submit(submit.submit_addr,submit.token,submit.success_request,submit.failed_request,message)

if __name__ == '__main__':
    import resolve_config
    con = resolve_config.main()
    flag = sys.argv[1]
    message = {'getflag_status': "getflag success", 'flag': flag}
    print(main(con.submit,message))
