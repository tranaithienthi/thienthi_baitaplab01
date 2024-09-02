# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 08:03:48 2024

@author: ASUS
"""

var=input("Nhập một chữ cái: ")
if len(var) == 1 and var.isalpha():
    if var.islower():
        var=var.upper()
        print("Bạn đã nhập:", var)
    elif var.isupper():
        var=var.lower()
        print("Bạn đã nhập: ", var)
else:
    print("Bạn chỉ được nhập 1 chữ cái duy nhất!")