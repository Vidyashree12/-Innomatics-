#!/usr/bin/env python
# coding: utf-8

# In[19]:


def fun(n):
    for i in range(1,n+1):
        print(i,end="")
fun(n=int(input()))


# ### Practice 

# In[5]:


n=int(input())
for i in range(1,n+1):
    print(i,end="")
    
    


# In[6]:


n=int(input())
def fun(n):
    for i in range(1,n+1):
        print(i,end="")
fun(n)


# In[8]:


#for Practice  
## using list compherension 
l=[x for x in range(1,int(input())+1)]
l


# In[14]:


## using *args
print(*(range(1,int(input())+1)),sep="")


# In[18]:


-note:
    1.range() function is used to generate a sequence of numbers.
    2. is a built-in function


# In[ ]:




