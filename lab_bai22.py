# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:30:11 2024

@author: ASUS
"""

a=float(input("a= "))
b=float(input("b= "))
if a==0:
    if b==0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else: 
    print("Phương trình có nghiệm là x= ", -b/a)
        

            