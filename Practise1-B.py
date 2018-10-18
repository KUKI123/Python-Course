#!/usr/bin/env python
# coding: utf-8

# In[9]:


x = float(input("Enter your number: "))

if (x < -100):
    print(-x)
elif (x >= -100 and x <= -25):
    print(x**4)
elif (x > -25 and x <= 0):
    print(3 * (x**2) - 1)
elif ( 0 < x and x <= 100):
    print((3.14/2)*x + 3**x)
elif ( x > 100):
    print(x)
    


# In[2]:


print("Hi")


# In[ ]:


x = int(input("Enter your number: "))

if (x < -100) :
    print(-x)
    
elif (x > 100):
    
    print(x)

