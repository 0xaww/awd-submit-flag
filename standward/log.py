import time

def write_log(localtime,ip,submit_status,getflag_status,flag_content):
    fd = open("run.log","a")
    fd.write(localtime +"\t" +  ip+"\t"+ getflag_status + "\t" + submit_status +"\t"+flag_content+"\n")
    fd.close()

def main(ip,message):
    getflag_status = message['getflag_status']
    submit_status = message['submit_status']
    flag_content = message['flag']
    localtime = time.asctime( time.localtime(time.time()) )
    if "success" in getflag_status:
        #print "this machine can be hacked"
        write_log(localtime,ip,submit_status,getflag_status,flag_content)
    else:
        #print "this machine can not be hacked"
        write_log(localtime,ip,submit_status,getflag_status,flag_content)

if __name__ == '__main__':
    main(ip,message)
