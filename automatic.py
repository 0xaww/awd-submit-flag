import os
import exp
import target
import exploit
import submit
import log
import time
import resolve_config

def clean():
    os.system("rm *.pyc")

def local_flag():
    fd = open("flag.txt","r")
    for line in fd:
        flag = line

    fd.close()

def main():
    #get config
    start_ip,end_ip,skip_ip,port,submit_addr,script_function,url_file,flag_file,round_time = resolve_config.main()
    ip_list = target.main(start_ip,end_ip,skip_ip)
    if script_function == "pwn":
        while 1:
            for ip in ip_list:
                message = exploit.main(ip,port)
                submit_status = submit.main(ip,port,message)
                message['submit_status'] = submit_status
                log.main(ip,message)
            time.sleep(round_time)
    elif script_function == "web":
        while 1:
            for url in url_file:
                flag = web_flag.main(url)
                submit_status = submit.main(ip,port,message)
                message['submit_status'] = submit_status
                log.main(ip,message)
            time.sleep(round_time)
    elif script_function == "local":
        while 1:
            for flag in flag_file:
                message = {'status':'success', 'flag': flag}
                submit_status = submit.main(ip,port,message)
                message['submit_status'] = submit_status
                log.main(ip,message)
            time.sleep(round_time)
    else:
        print "script_function set error"
    clean()


if __name__ == '__main__':
    main()
