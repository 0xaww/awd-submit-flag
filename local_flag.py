from pwn import *
def main(ip,port):
    try:
        fd = open("flag.txt","r")
        for line in fd:
            flag = line
        fd.close()
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception, e:
        a = str(e)
        return {'status':"failed"+a, 'flag':'no flag'}
    return {'status':'success', 'flag': flag}

if __name__ == '__main__':
    main(ip,port)
