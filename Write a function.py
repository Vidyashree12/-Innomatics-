#!/usr/bin/env python
# coding: utf-8

# In[13]:


def is_leap(year):
    
    
    # Write your logic here
    if (( year%4==0 and  year%100==0 and year%400==0)):
        return True
    else:
        return False


        



year = int(input())
print(is_leap(year))


# ================================== Check -================================
# 
# 
# 1800, 1900, 2100, 2200, 2300 and 2500---- Not Leap year
# 
# 2000 and 2400 -- Leap year
