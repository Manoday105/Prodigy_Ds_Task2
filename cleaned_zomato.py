#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv('Zomato.csv')
data.head()


# In[5]:


data.shape


# In[6]:


data.columns


# In[8]:


data=data.drop(['url', 'phone', 'address', 'menu_item', 'dish_liked', 'reviews_list'], axis=1)
print('Done')


# In[9]:


data.info()


# In[10]:


data.drop_duplicates(inplace = True)


# In[12]:


data.shape


# In[13]:


data['rate'].unique()


# In[18]:


def CorrectRate(value):
    if value == 'NEW' or value == '-':
        return np.nan
    else:
        value=str(value).split('/')
        value=value[0] # there will be a split at '/' and a list will be created where we'll be having a float and 5. We are interested in float value only which is present at index=0
        return float(value)
data['rate']= data['rate'].apply(CorrectRate)
data.head()


# In[19]:


data.rate.isnull().sum()


# In[21]:


data['rate'].fillna(data['rate'].mean(),inplace = True)
data.rate.isnull().sum()


# In[22]:


data.info()


# In[23]:


data.dropna(inplace = True)


# In[24]:


data.head()


# In[25]:


data.rename(columns ={'approx_cost(for two people)':'cost2people','listed_in(type)':'type'},inplace = True)


# In[26]:


data.head()


# In[27]:


data['location'].unique()


# In[29]:


data=data.drop(['listed_in(city)'], axis=1)


# In[31]:


data['cost2people'].unique()


# In[33]:


def CorrectComma(value):
    value=str(value)
    if ',' in value:
        value=value.replace(',', '')
        return float(value)
    else:
        return float(value)
data['cost2people']=data['cost2people'].apply(CorrectComma)
data['cost2people'].unique()


# In[34]:


data['location'].value_counts()


# In[35]:


location=data['location'].value_counts(ascending=False)
LocationLessThan300 = location[location<300]

def CorrectLocation(value):
    if (value in LocationLessThan300):
        return 'others'
    else:
        return value
data['location']=data['location'].apply(CorrectLocation)
data['location'].value_counts()


# In[36]:


data.head()


# In[37]:


cuisines = data['cuisines'].value_counts(ascending=True)
CuisinesLessThan100 = cuisines[cuisines<100]

def CorrectCuisines(value):
    if(value in CuisinesLessThan100):
        return 'others'
    else:
        return value
        
data['cuisines'] = data['cuisines'].apply(CorrectCuisines)
data['cuisines'].value_counts()


# In[38]:


data.to_csv('cleaned_zomato.csv',index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




