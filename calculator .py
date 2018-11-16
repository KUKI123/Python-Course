#!/usr/bin/env python
# coding: utf-8

# In[2]:



import math
# Program make a simple calculator that can add, subtract, multiply and divide,exponent, sequare root, 
# trigeminal, log and using functions

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y
# This function exponential two numbers
def exp(x,y):
   return x**y
# This function sin two numbers
def sin(x):
   return sin(x)
# This function cos two numbers
def cos(x):
    return cos(x)
# This function tan two numbers
def tan(x):
    return tan(x)
# This function sequare root two numbers
def sqr(x):
    return x**(0.5)
# This function log two numbers
def log(x):
    return log(x)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exp")
print("6.sin")
print("7.cos")
print("8.tan")
print("9.square")
print("10.log")

# Take input from the user 
choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
   print(num1,"exp",num2,"=", f(num1,num2))
elif choice == '6':
   print(num1,"sin =", math.sin(num1))
   print(num2,"sin =", math.sin(num2))
elif choice == '7':
   print(num1,"cos =", math.cos(num1))
   print(num2,"cos =", math.cos(num2))
elif choice == '8':
   print(num1,"tan =", math.tan(num1))
   print(num2,"tan =", math.tan(num2))
elif choice == '9':
   print(num1,"sqr =", (num1)**(0.5))
   print(num2,"sqr =", (num2)**(0.5))

elif choice == '10':
   print(num1,"log =", math.log(num1))
   print(num2,"log =", math.log(num2))


else:
   print("Invalid input")
print("_______________")
print("Programming By Ikram")

