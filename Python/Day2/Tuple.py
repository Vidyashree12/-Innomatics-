#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
integer_list = tuple(map(int,raw_input().split()))
print( hash(integer_list))

