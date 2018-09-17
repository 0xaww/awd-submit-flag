def write_log(ip,submit_status,getflag_status,flag_content):
    fd = open("automatic.log","a")
    fd.write(ip+"\t\""+ getflag_status + "\"\t\"" + submit_status +"\"\t"+flag_content+"\n")
    fd.close()

def main(ip,message):
    getflag_status = message['getflag_status']
    flag_content = message['flag']
    submit_status = message['submit_status']
    if "success" in getflag_status:
        #print "this machine can be hacked"
        write_log(ip,submit_status,getflag_status,flag_content)
    else:
        #print "this machine can not be hacked"
        write_log(ip,submit_status,getflag_status,flag_content)

if __name__ == '__main__':
    main(ip,message)
