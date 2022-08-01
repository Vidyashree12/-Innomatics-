#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def split_and_join(line):
    # write your code her
    str1=line.split(" ")
    str1="-".join(str1)
    return str1
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

