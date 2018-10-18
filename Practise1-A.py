#!/usr/bin/env python
# coding: utf-8

# In[1]:


A = input("Enter your Name: ")
X = input("Enter the first Number: ")
Y = input("Enter the Second Number: ")

print("Hi Mr/Mrs " + A + ",")
print("The Sum of "+str(X)+" and " + str(Y) + (" is: ") + str(int(X) + int(Y)))
print("The Sub of "+str(X)+" and " + str(Y) + (" is: ") + str(int(X) - int(Y)))
print("The Mul of "+str(X)+" and " + str(Y) + (" is: ") + str(int(X) * int(Y)))
print("The Div of "+str(X)+" over " + str(Y) + (" is: ") + str(int(X) / int(Y)))
print("The Reminder of "+str(X)+" over " + str(Y) + (" is: ") + str(int(X) % int(Y)))
print("The Exponent of "+str(X)+" to the power of " + str(Y) + (" is: ") + str(int(X) ** int(Y)))

