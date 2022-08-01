#!/usr/bin/env python
# coding: utf-8

# In[13]:


# understanding 

x = int(input())
y = int(input())
z = int(input())
n = int(input())

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
              print([i,j,k])


# In[11]:


for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if(i+j+k)!=n:
                print([i,j,k],end=",") 


# ## Hackerrank Solution 

# In[4]:


# using list compherension 
x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])


# In[ ]:





# In[ ]:




