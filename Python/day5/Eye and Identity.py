#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
numpy.set_printoptions(legacy="1.13")
N,M=map(int,(input().split()))

print(numpy.eye(N,M))

