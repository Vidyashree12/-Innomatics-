#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for _ in range(n)],int)
min1=numpy.min(a,axis=1)
print(numpy.max(min1))

