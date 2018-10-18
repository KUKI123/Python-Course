#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=1
while 1==1:
    print("1. for convert celsius to fehrenheit")
    print("2. for convert fehrenheit to celsius")
    num=int(input("enter your number"))
    
if(num==1):
    c=int(input("enter celsius temp. = "))
    f=(c*9/5)+32
    print("fehrenheit temp. =",f)
    
if(num==2):
    f=int(input("enter fehrenheit temp. ="))
    c=(f-32)*5/9
    print("celsius temp. =",c)
    
if(num>=3):
    print("enter valid number")
    a=0

