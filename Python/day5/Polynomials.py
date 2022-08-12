#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
p=numpy.array(input().split(),float)
x=float(input())
print(numpy.polyval(p,x))

