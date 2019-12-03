import struct
import socket

def findIPs(start, end):
    ipstruct = struct.Struct('>I')
    start, = ipstruct.unpack(socket.inet_aton(start))
    end, = ipstruct.unpack(socket.inet_aton(end))
    return [socket.inet_ntoa(ipstruct.pack(i)) for i in range(start, end+1)]

def main(ip_mode ,start_ip ,end_ip ,skip_ip):
    ip_list=[]
    for i in range(int(start_ip) ,int(end_ip)+1):
        url = ip_mode % i
        if str(i) in skip_ip:
            continue
        ip_list.append(url)
    return ip_list


if __name__ == '__main__':
    main(ip_mode ,start_ip ,end_ip,skip_ip)
