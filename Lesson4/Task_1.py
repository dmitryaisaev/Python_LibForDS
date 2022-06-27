#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[16]:


import matplotlib.pyplot as plt


# In[11]:


a = [i for i in range(1,8)]
a


# In[12]:


b = [3.5, 3.8, 4.2, 4.5, 5, 5.5, 7]
b


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


plt.plot(a, b)


# In[19]:


plt.scatter(a, b)
plt.show

