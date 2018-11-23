from socket import *
from time import ctime

host = '' #监听所有的ip
#port = 13141 #接口必须一致
port = 4097
bufsize = 1024
addr = (host,port)

udpServer = socket(AF_INET,SOCK_DGRAM)
udpServer.bind(addr) #开始监听

while True:
    print('Waiting for connection...')
    data,addr = udpServer.recvfrom(bufsize)  #接收数据和返回地址

    print(data)
    udpServer.sendto(data,addr)

    print(data,'...recevied from and return to :',addr)

udpServer.close()
