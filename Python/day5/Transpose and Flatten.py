#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
N,M=map(int,input().split())
arr=np.array([input().strip().split() for _ in range(N)], int)
print (arr.transpose())
print (arr.flatten())

