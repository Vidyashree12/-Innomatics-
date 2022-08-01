#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[]

for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
print(sorted(list([score,name] for name , score in l))[1][1])


# In[ ]:




