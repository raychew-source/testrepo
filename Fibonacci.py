#!/usr/bin/env python
# coding: utf-8

# In[6]:


def fib (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# In[7]:


print(fib(0))


# In[8]:


print(fib(1))


# In[10]:


print(fib(2))


# In[11]:


print(fib(6))


# In[ ]:




