# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:11:49 2024

@author: ASUS
"""

a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c=float(input("Nhập số c: "))
if a>b and a>c:
    print(f"Số  nhất là: {a}")
elif b>a and b>c:
    print(f"Số nhỏ nhất là: {b}")
else:
    print(f"Số lớn nhất là: {c}")
