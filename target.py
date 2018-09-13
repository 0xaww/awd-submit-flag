import struct
import socket

def input():
    #input or fixed

    #startip = raw_input('please input start IPaddress(example:192.168.1.1):')
    #endip = raw_input('please input end IPaddress(example:192.168.1.255):')
    #port = raw_input('please input port(example:9999):')

    #fixed
    startip = "127.0.0.1"
    endip = "127.0.0.2"
    port = 9999
    return startip,endip,port

def findIPs(start, end):
    ipstruct = struct.Struct('>I')
    start, = ipstruct.unpack(socket.inet_aton(start))
    end, = ipstruct.unpack(socket.inet_aton(end))
    return [socket.inet_ntoa(ipstruct.pack(i)) for i in range(start, end+1)]

def main():
    startip ,endip ,port = input()
    ip_list = findIPs(startip ,endip)
    return startip , endip , port , ip_list


if __name__ == '__main__':
    main()
