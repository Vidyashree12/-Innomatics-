#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy

n,m=map(int,input().split())
a=numpy.array([input().split() for _ in range(n)],int)

print(numpy.mean((a),axis=1))
print(numpy.var(a,axis=0))
print(round(numpy.std(a,axis=None),11))

