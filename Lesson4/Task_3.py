#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


# In[15]:


x = np.linspace(-3, 3, 51)
x


# In[17]:


y1 = x**2
y2 = 2 * x + 0.5
y3 = -3 * x - 1.5
y4 = np.sin(x)


# In[29]:


fig, ax = plt.subplots(nrows = 2, ncols = 2)
ax1, ax2, ax3, ax4 = ax.flatten()

ax1.plot(x, y1)
ax1.set_title('Графиеп y1')
ax1.set_xlim([-5, 5])

ax2.plot(x, y2)
ax2.set_title('Графиеп y2')

ax3.plot(x, y3)
ax3.set_title('Графиеп y3')

ax4.plot(x, y4)
ax4.set_title('Графиеп y4')

fig.set_size_inches(8, 6)
plt.subplots_adjust(wspace=0.3, hspace=0.3)


# In[ ]:




