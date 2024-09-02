# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:17:00 2024

@author: ASUS
"""

a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c=float(input("Nhập số c: "))
if a>b and b>a:
    print(f"Thứ tự tăng dần là: {c},{b},{a}")
elif b>a and a>c:
    print(f"Thứ tự tăng dần là: {c},{a},{b}")
elif b<a and a<c:
    print(f"Thứ tự tăng dần là: {b},{a},{c}")
elif b<c and c<a:
    print(f"Thứ tự tăng dần là: {b},{c},{a}")
elif a<b and a<c:
    print(f"Thứ tự tăng dần l: {a},{b},{c}")
else:
    print(f"Thứ tự tằn dần là: {a},{c},{b}")
    