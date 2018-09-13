def write_log(ip,message_content,flag_content):
    fd = open("automatic.log","a")
    fd.write(ip+"\t"+message_content+"\t"+flag_content+"\n")
    fd.close()

def main(ip,message):
    message_content = message['status']
    flag_content = message['flag']
    submit_status = message['submit_status']
    if "success" in message_content:
        #print "this machine can be hacked"
        write_log(ip,message_content,flag_content)
    else:
        #print "this machine can not be hacked"
        write_log(ip,message_content,flag_content)

if __name__ == '__main__':
    main(ip,message,flag)
