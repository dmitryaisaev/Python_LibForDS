#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


# In[5]:


t = np.linspace(0, 10, 51)
t


# In[8]:


f = np.cos(t)
f


# In[14]:


plt.plot(t, f, color = 'green')
plt.axis([0.5, 9.5, -2.5, 2.5])
plt.title('График f(t)')
plt.xlabel('Значения t')
plt.ylabel('Значения f')
plt.show()


# In[ ]:




