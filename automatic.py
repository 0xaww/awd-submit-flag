import os
import time
import pwn_attack
import web_attack
import submit
import log
import resolve_config

def clean():
    os.system("rm *.pyc")


def main():
    #get config
    con = resolve_config.main()
    if con.script_function == "pwn":
        while 1:
            for ip in con.ip_list:
                message = pwn_attack.main(ip)
                message = submit.main(con.submit,message)
                log.main(ip,message)
                time.sleep(con.submit_wait)
            time.sleep(con.round_time)
    elif con.script_function == "web":
        while 1:
            for ip in con.ip_list:
                message = web_attack.main(ip)
                message = submit.main(con.submit,message)
                log.main(ip,message)
                time.sleep(con.submit_wait)
            time.sleep(con.round_time)
    elif con.script_function == "local":
        while 1:
            for flag in con.flag_list:
                message = {'getflag_status':'getflag success', 'flag': flag}
                message = submit.main(con.submit,message)
                log.main(flag,message)
                time.sleep(con.submit_wait)
            time.sleep(con.round_time)
    else:
        print "script_function set error"
    clean()


if __name__ == '__main__':
    main()
    clean()
