import os
import exp
import target
import exploit
import submit
import log
import time

def clean():
    os.system("rm *.pyc")


def main():
    while 1:
        startip , endip , port ,skip_ip , ip_list = target.main()
        for ip in ip_list:
            if ( ip in skip_ip):
                continue
            message = exploit.main(ip,port)
            submit.main(ip,message,token=0)
            log.main(ip,message)
        clean()
        time.sleep(300)#set round time

if __name__ == '__main__':
    main()
