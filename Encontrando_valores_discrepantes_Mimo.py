#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Vericamos se um numero é um valor atipico no conjunto de dados e definimos a variavel oulier como Verdadeiro, caso fosse


# In[ ]:


upper_limit = 91


# In[2]:


lower_limit = 24


# In[3]:


outlier = False


# In[4]:


number = 8


# In[6]:


if number > upper_limit:
    outlier = True
if number < lower_limit:
    outlier = True
if outlier == True:
    print(f"{number} is an outlier")


# In[ ]:




