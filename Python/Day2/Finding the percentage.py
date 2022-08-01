#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input())
Student_Record={}
for _ in range(n):
   names,*line=(input().split())
   score=list(map(float,line))
   Student_Record[names]=score
query_name=input()
total=sum(Student_Record[query_name])
average=total/3
print("{:.2f}".format(average))


# In[ ]:




