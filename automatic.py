import os
import exp
import target
import exploit
import submit
import log

def clean():
    os.system("rm *.pyc")


def main():
    startip , endip , port ,skip_ip , ip_list = target.main()
    for ip in ip_list:
        if ( ip in skip_ip):
            continue
        message = exploit.main(ip,port)
        submit.main(ip,message,token=0)
        log.main(ip,message)
    clean()

if __name__ == '__main__':
    main()
