#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def arrays(arr):
    # complete this function
    return(numpy.array(numpy.flip(arr), float))

    # use numpy.array
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

