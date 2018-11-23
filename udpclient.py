"""
author: Fan Zhang
created on : 2018-11-23
"""
import sys
from socket import *
from cmd_decoder import *


host  = '10.160.36.185' # 这是客户端的电脑的ip
#host  = '127.0.0.1' # 这是客户端的电脑的ip
#port = 13141 #接口选择大于10000的，避免冲突
port = 4097
bufsize = 1024  #定义缓冲大小

addr = (host,port) # 元祖形式
udpClient = socket(AF_INET,SOCK_DGRAM) #创建客户端

CardNo = int(sys.argv[1])
RW = int(sys.argv[2])

RegAddr_s = sys.argv[3]
if RegAddr_s[0:2] == '0x' :
    RegAddr = int(RegAddr_s,16)
else :
    RegAddr = int(RegAddr_s,10)

RegData_s = sys.argv[4]
if RegData_s[0:2] == '0x' :
    RegData = int(RegData_s,16)
else :
    RegData = int(RegData_s,10)

while True:
    switch = input('Enter start:')
    data = cmd_decoder(CardNo,RW, RegAddr,RegData)
    if not data:
        break
    udpClient.sendto(data,addr) # 发送数据

    if RW == 1 :
        data,addr = udpClient.recvfrom(bufsize) #接收数据和返回地址
        data_s = data.hex()
        print('Register addr is: 0x',data_s[0:8])
        print('Register data is: 0x',data_s[8:16])
    else:
        print('Register WRITE finished')

udpClient.close()
