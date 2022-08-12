#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
n,m=map(int,input().split())
B=numpy.sum((numpy.array([input().split() for _ in range(n)],int)),axis=0)
print(numpy.prod((B),axis=0))

