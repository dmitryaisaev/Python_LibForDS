#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[12]:


ccfd = pd.read_csv('creditcard.csv')
ccfd.shape


# In[4]:


x = ccfd['Class'].value_counts()
x


# In[16]:


plt.style.use('fivethirtyeight')


# In[17]:


x.plot(kind='barh')
plt.show()


# In[18]:


x.plot(kind='barh', logx=True)
plt.show()


# In[19]:


v1c0 = ccfd.loc[ccfd['Class'] == 0, 'V1']
v1c1 = ccfd.loc[ccfd['Class'] == 1, 'V1']


# In[47]:


h = plt.hist([v1c0, v1c1], bins=20, ec='white', color=['grey', 'red'], density=True, alpha=0.5)
plt.xlabel('V1')
plt.legend(labels=['Class 0', 'Class 1'])
plt.show()


# In[ ]:




