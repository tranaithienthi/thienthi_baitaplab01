# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:35:12 2024

@author: ASUS
"""

a=int(input("Nhập 4 số xe của bạn: "))
if a>999 and a<=9999:
    b=a//1000
    c=a%1000
    d=c//100
    e=c%100
    f=e//10
    t=e%10
    s=b+d+f+t
    if s>10 and s<=36:
        print("Số nút xe của bạn là: ", s%10)
    else:
        print("Số nút xe của bạn là: ", s)
else:
    print("Vui lòng nhập số có 4 chữ số!")
    
