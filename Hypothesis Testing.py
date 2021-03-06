#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy.stats import norm
import pandas_datareader as web
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


ms = web.DataReader('MSFT', data_source='yahoo', start='1990-05-01')
ms['logReturn'] = np.log(ms['Close'].shift(-1)) - np.log(ms['Close'])


# In[3]:


ms['logReturn'].plot(figsize=(20, 8))
plt.axhline(0, color='red')
plt.show()


# In[4]:


sample_mean = ms['logReturn'].mean()
sample_std = ms['logReturn'].std(ddof=1)
n = ms['logReturn'].shape[0]

zhat = (sample_mean - 0)/(sample_std/n**0.5)
print(zhat)


# In[5]:


alpha = 0.05

zleft = norm.ppf(alpha/2, 0, 1)
zright = -zleft
print(zleft, zright)


# In[6]:


print('At significant level of {}, shall we reject: {}'.format(alpha, zhat>zright or zhat<zleft))


# In[7]:


sample_mean = ms['logReturn'].mean()
sample_std = ms['logReturn'].std(ddof=1)
n = ms['logReturn'].shape[0]

zhat = (sample_mean-0)/(sample_std/(n**0.5))
print(zhat)


# In[8]:


alpha = 0.05

zright =norm.ppf(1-alpha, 0, 1)
print(zright)


# In[9]:


print('At a significant level of {}, shall we reject {}'.format(alpha, zhat>zright))


# In[10]:


p = 1 - norm.cdf(zhat, 0, 1)
print(p)


# In[13]:


print('At a significant level of {}, shall we reject: {}'.format(alpha, p < alpha))


# In[ ]:




