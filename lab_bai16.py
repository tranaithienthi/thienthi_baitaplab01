# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:09:59 2024

@author: ASUS
"""

a=input("Nhập thời gian: ")
if "h" in a:
    gio=int(a.split('h')[0])
    a=a.split('h')[1]
if "p" in a:
    phut=int(a.split("p")[0])
    a=a.split("p")[1]
if "s" in a:
    giay=int(a.split("s")[0])
    a=a.split("s")[1]
ket_qua=gio*3600+phut*60+giay
print(f"Tổng số giây là: {ket_qua}")

