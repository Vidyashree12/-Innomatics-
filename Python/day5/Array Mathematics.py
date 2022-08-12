#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
N,M=map(int,input().split())
A=numpy.array([input().split()for _ in range(N)],int) 
B=numpy.array([input().split()for _ in range(N)],int)
print(A+B, A-B, A*B, A//B, A%B, A**B, sep='\n') 

