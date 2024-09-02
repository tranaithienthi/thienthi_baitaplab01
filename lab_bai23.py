# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:59:18 2024

@author: ASUS
"""

import math
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
if a!=0:
   delta=(b*b)-4*a*c
   if delta>0:
       x1=(-b+math.sqrt(delta))/(2*a)
       x2=(-b-math.sqrt(delta))/(2*a)
       print(f"Phương trình có 2 nghiệm phân biệt: x1={x1} và x2={x2}")
   elif delta==0:
       print("Phương trình có một nghiệm kép: x1=x2=",-b/2*a)
   else:
       print("Phương trình vô nghiệm")
else:
    if b != 0:
        x = -c / b
        print(f"Phương trình trở thành phương trình bậc nhất và có nghiệm là: {x}")
    else:
        print("Phương trình vô nghiệm hoặc có vô số nghiệm (nếu c = 0)")
        