import struct
import socket

#def input():
    #input or fixed

    #startip = raw_input('please input start IPaddress(example:192.168.1.1):')
    #endip = raw_input('please input end IPaddress(example:192.168.1.255):')
    #port = raw_input('please input port(example:9999):')

    #fixed
    #skip_ip = ("127.0.0.11","127.0.0.15")
    #startip = "127.0.0.1"
    #endip = "127.0.0.255"
    #port = 9999
    #return startip,endip,skip_ip,port

def findIPs(start, end):
    ipstruct = struct.Struct('>I')
    start, = ipstruct.unpack(socket.inet_aton(start))
    end, = ipstruct.unpack(socket.inet_aton(end))
    return [socket.inet_ntoa(ipstruct.pack(i)) for i in range(start, end+1)]

def main(start_ip ,end_ip ,skip_ip):
    #startip ,endip ,skip_ip  = input()
    ip_list = findIPs(start_ip ,end_ip)
    for ip in skip_ip:
        ip_list.remove(ip)
    return ip_list


if __name__ == '__main__':
    main(start_ip ,end_ip,skip_ip)
