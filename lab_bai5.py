# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:42:36 2024

@author: ASUS
"""

var=input("Nhập vào giờ, phút và giây (hh:mm:ss): ")
hh,mm,ss = map(int, var.split(':'))
a=hh*3600+mm*60+ss
print(f"Tổng số giây: {a}")
