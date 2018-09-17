import os
import pwn_flag
import target
import web_flag
import submit
import log
import time
import resolve_config

def clean():
    os.system("rm *.pyc")


def main():
    #get config
    start_ip,end_ip,skip_ip,port,submit_addr,script_function,url_file,flag_file,round_time,token,success_request,failed_request,flag_start,flag_end = resolve_config.main()
    ip_list = target.main(start_ip,end_ip,skip_ip)
    if script_function == "pwn":
        while 1:
            for ip in ip_list:
                message = pwn_flag.main(ip,port)
                submit_status = submit.main(submit_addr,message,token,success_request,failed_request)
                message['submit_status'] = submit_status['status']
                log.main(ip,message)
            time.sleep(round_time)
    elif script_function == "web":
        while 1:
            for url in url_file:
                message = web_flag.main(url,flag_start,flag_end)
                submit_status = submit.main(submit_addr,message,token,success_request,failed_request)
                message['submit_status'] = submit_status['status']
                log.main(url,message)
            time.sleep(round_time)
    elif script_function == "local":
        while 1:
            for flag in flag_file:
                message = {'getflag_status':'getflag success', 'flag': flag}
                submit_status = submit.main(submit_addr,message,token,success_request,failed_request)
                message['submit_status'] = submit_status['status']
                log.main(flag,message)
            time.sleep(round_time)
    else:
        print "script_function set error"
    clean()


if __name__ == '__main__':
    main()
