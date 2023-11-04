#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[6]:


string="abc00123xyz456"


# In[4]:


pattern=('^[a-zA-Z0-9]*$')


# In[7]:


matches=re.match(pattern,string)
print(matches)


# In[22]:


string="adbddddbbb"
pattern=('a.*?b$')
matches=re.match(pattern,string)
print(matches)


# In[35]:


string="India is my motherland"
pattern=("motherland$")
matches=re.findall(pattern,string)
if matches:
    print("Y")
else:
        print("N")


# In[69]:


string=('01 0132 231875 1458 301 2725')
pattern=(r'\b\d{4}\b')
matches=re.findall(pattern,string)
print(matches)


# In[ ]:




