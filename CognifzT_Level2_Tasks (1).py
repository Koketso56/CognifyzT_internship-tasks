#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np 

data = r"C:\Users\koket\Downloads\Dataset .csv"

df = pd.read_csv(data)

df.describe()


# In[15]:


agg_ratings = df.groupby("Aggregate rating").describe()
agg_ratings


# # THE MOST COMMON RATING RANGE IS 3.3 TO 3.5

# In[27]:


votes = df.groupby("Votes")["Restaurant Name"].value_counts()
result = np.average(votes)
result 


# # TASK 2

# In[6]:


Cuisines = df.groupby("Cuisines").describe(include="all")
Cuisines


# In[14]:


results = Cuisines.sort_values(by="Cuisines")
results


# In[15]:


results.head(50)


# In[16]:


df_cuisines1 = df.value_counts("Cuisines")
df_cuisines1.head(50)


# # SOME OF THE MOST COMMON COMBINATIONS OF CUISINES ARE: NORTH INDIAN & CHINESE, NORTH INDIAN & MUGHLAI, NORTH INDIAN & MUGHLAI & CHINESE, AND BAKERY & DESSERTS

# In[22]:


high_ratings = df.groupby("Cuisines")["Aggregate rating"].describe()
high_ratings


# In[23]:


high_ratings.tail(50)


# In[24]:


high_ratings.head(50)


# # YES, WE HAVE SOME COMBINATIONS, WHICH ARE TIBETAN & CHINESE, AND AMERICAN BURGER

# # TASK 3

# In[26]:


pip install folium


# In[28]:


pip install folium


# In[8]:


import folium

longitude = df["Longitude"].dropna()
latitude = df["Latitude"].dropna()

result = folium.Map(location = [latitude, longitude])

result.save("CognifyzT.html")


# In[ ]:




