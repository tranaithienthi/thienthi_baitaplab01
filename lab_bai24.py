# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:21:29 2024

@author: ASUS
"""

a=int(input("Nhập giờ: "))
b=int(input("Nhập phút: "))
c=int(input("Nhập giây: "))
if 0<a<=24:
    b>0 and b<=60
    c>0 and c<=60
    print("Nhập liệu hợp lệ!")
else:
    print("Nhập liệu không hợp lệ!")