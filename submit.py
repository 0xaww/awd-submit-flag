from pwn import *

def main(ip,message,token=0):
    flag_content = message['flag']
    ##submit flag
    os.system("echo "+flag_content)

    ##curl 
    #os.system("curl -k 'https://172.16.4.1/Common/awd_sub_answer' -d 'token=35c6f7e1adbbdc0acd8850119c8c0d52&answer='"+flag_content+" -X POST")


if __name__ == '__main__':
    main(ip,message,token=0)
