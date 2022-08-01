#!/usr/bin/env python
# coding: utf-8

# In[16]:


n = int(input())
for i in range(0,n):
   
    print(i**2)


# In[17]:





# In[21]:


n=int(input())
if(n%2==0 and range(6,21)):
    print("Weird")
else:
    print("Not Weird")


# In[26]:


n = int(input())
if(n%2!=0):
   print("Weird")
elif(n%2==0 and n in range(2,6)):
   print("Not Weird")
   
elif(n%2==0 and n in range(6,21) or n>20):
   print("Weird")
else:
   print("Not Weird")


# In[25]:


18>20


# In[ ]:




