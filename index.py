#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = {
    "F_name" : ["Jon", "Wink", "Paul", "Loop"],
    "L_name" : ["Kim", "Zam", "Un", "All"],
    "Email"  : ["Jonkim@email.com", "Winkzam@email.com", "Paulun@email.com", "Loopall@email"]
}


# In[5]:


dataset = pd.DataFrame(df)
dataset


# In[9]:


dataset['Email']


# In[10]:


dataset.shape


# In[11]:


dataset.index


# In[12]:


dataset[["F_name", "Email"]]


# In[13]:


dataset.set_index("F_name", inplace = True)


# In[17]:



dataset.head(1)


# In[19]:


dataset.value_counts("Email")


# In[20]:


dataset.sort_index()


# In[21]:


dataset.sort_index(ascending = False)


# In[22]:


type(dataset["Email"])


# In[25]:


dataset.loc["Jon"]


# In[26]:


dataset.loc[["Jon", "Paul"], "Email"]


# In[33]:


dataset.loc["Jon", "Email"]


# In[34]:


dataset.reset_index(inplace = True)


# In[36]:


dataset.head(1)


# In[40]:


dataset[dataset['F_name'] == "Jon"]


# In[46]:


filt = (dataset["L_name"] == "Un")


# In[48]:


dataset.loc[filt]


# In[49]:


dataset


# In[53]:


filt = (dataset['F_name'] == 'Jon') & (dataset['L_name'] == 'Kim')


# In[54]:


dataset.loc[filt, 'Email']


# In[55]:


dataset.loc[~filt, 'Email']


# In[57]:


data = pd.read_csv(r"D:\All years (Weekly Fuel Prices).csv", index_col = "Date")
data.head()


# In[59]:


data.dtypes


# In[62]:


data.value_counts('Diesel/Petrol')


# In[63]:


filt = (data['Pump Price in euro'] > 100 )
data.loc[filt]


# In[65]:


data.reset_index(5 )


# In[66]:


data.head()


# In[67]:


data.index


# In[69]:


data.iloc[0, 1]


# In[71]:


data.sort_index(ascending = False)


# In[73]:


data[data.isnull()]


# In[74]:


get_ipython().run_line_magic('pinfo', 'DATA.DTYPES')


# In[80]:


data


# In[81]:


data.reset_index(inplace = True)
data

