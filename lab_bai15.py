# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:58:11 2024

@author: ASUS
"""

import math
a=float(input("Nhập số a:"))
b=float(input("Nhập số b: "))
c=((a+b)/(a)**(1/3))-(((a*b)*(1/3)))
d=(a**(1/3))-(b**(1/3))
e=math.sqrt(d)
print("Kết quả của biểu thức là: ", c/e)