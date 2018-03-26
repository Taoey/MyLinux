#!/usr/bin/env python3
#coding:utf-8
"""
需求：
1.把ip地址号修改为可读性的二进制字符流，例如"123.123.123.123" --> "0111,1011*0111,1011&0111,1011*0111,1011"
2.每个数据到要用8位代表，例如"15"需要表示为"0000,1111"

"""
if __name__ == '__main__':

    while True :
        ip = input("Please input IP :")
        # ip = "123.123.123.123"
        strList = ip.split(".")
        binList = []
        result = ""
        try:
            for i in strList:
                r = '{:08b}'.format(int(i))
                r = r[:4]+","+r[4:]
                binList.append(r)
            result = "*".join(binList)
            print(result)
        except :
            print("error!!!")

