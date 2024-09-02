# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:51:23 2024

@author: ASUS
"""

a=int(input("Nhập ngày sinh của bạn: "))
b=int(input("Nhập tháng sinh của bạn: "))
c=int(input("Nhập năm sinh của bạn: "))
print(f"Ngày/tháng/năm của bạn là:{a}/{b}/{c}")
c=str(c)
print(f"Ngày/tháng/năm của bạn là:{a}/{b}/{c[-2:]}")
print(f"Ngày/tháng/năm của bạn là:{c}/{b}/{a}")