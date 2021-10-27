#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


cars =pd.read_csv('mtcars.csv')


# In[6]:


cars


# In[8]:


cars.shape


# In[9]:


cars.describe()


# In[10]:


# table 
pd.crosstab(cars.gear,cars.cyl)


# In[11]:


cars_4 = cars[(cars.gear==3) & (cars.cyl==4)] #  and operation (&)
cars_4


# In[12]:


pd.crosstab(cars.gear,cars.cyl).plot(kind="bar")


# In[13]:


cars.cyl.value_counts()


# In[14]:


cars.gear.value_counts()


# In[15]:


cars.gear.value_counts().plot(kind="pie") 


# In[16]:


cars["gear"].value_counts()


# In[17]:


import seaborn as sns


# In[19]:


sns.boxplot(x="gear",y="mpg",data=cars)


# In[21]:


sns.pairplot(cars.iloc[:,0:4])


# In[ ]:




