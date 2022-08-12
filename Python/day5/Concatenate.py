#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
N,M,P=map(int,input().split())
 
arr=numpy.array([input().split() for _  in range(N)],int)
arr2=numpy.array([input().split()for _ in range(M)],int)
print(numpy.concatenate((arr,arr2)))

