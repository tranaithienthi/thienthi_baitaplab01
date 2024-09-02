# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:27:36 2024

@author: ASUS
"""

import math
A=input("Nhập hình bạn muốn tính chu vi và diện tích với hình vuông(v), hình chữ nhật(n), hình tròn là(t): ")
if A=="v":
    a=input("Cạnh hình vuông là: ")
    S=a*a
    P=a+a+a+a
    print(f"P={P}, S={S}")
elif A=="n":
    a=float(input("Chiều dài của hình chữ nhật là: "))
    b=float(input("Chiều rộng của hình chữ nhật là: "))
    S=a*b
    P=(a+b)*2
    print(f"S={S}, P={P}")
elif A=="t":
    a=float(input("Bán kính hình tròn là: "))
    pi=math.pi
    S=2*pi*a
    P=a*a*pi
    print(f"S={S}, P={P}")
else:
    print("Nhập liệu không hợp lệ!")
    
    