#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np

data = r"C:\Users\koket\Downloads\Dataset .csv"
df = pd.read_csv(data)
df.describe(include="all")
print(df)

df_cuisines = df["Cuisines"].describe() 

Cuisines = df["Cuisines"].copy()

df_cuisines1 = df.value_counts("Cuisines")

print("The top common cuisine in the dataset are:")
print(df_cuisines1.head(50))


# # THE TOP 3 COMMON CUISINES ARE NORTH INDIAN, NORTH INDIAN & CHINESE, AND FINALLY, CHINESE

# In[2]:


perce = df.groupby("Cuisines")["Restaurant Name"].value_counts()
perce


# In[3]:


total = df["Restaurant Name"].count() / perce.loc["North Indian"].count() * 100
total


# In[4]:


total_2 = df["Restaurant Name"].count() / perce.loc["North Indian, Chinese"].count() * 100
total_2


# In[5]:


total_3 = df["Restaurant Name"].count() / perce.loc["Chinese"].count() * 100
total_3


# In[6]:


new_df1 = print(f'Percentage of restaurants that serve the North Indian cuisine : {total}%')
new_df2 = print(f'Percentage of restaurants that serve the North Indian & Chinese cuisine : {total_2}%')
new_df2 = print(f'Percentage of restaurants that serve the Chinese cuisine : {total_3}%')


# # TASK 2 

# In[7]:


import pandas as pd 

data = r"C:\Users\koket\Downloads\Dataset .csv"

df = pd.read_csv(data)

#detailed specifications about the data, tells us things like, count,frequency,top,etc
df_city = df["City"].describe()

City = df.groupby("City")["Restaurant Name"].count()

City.sort_values(ascending=False)


# # THE CITY WITH THE HIGHEST NUMBER OF RESTAURANTS IS NEW DELHI BY 5473 

# In[8]:


task_2 = df.groupby("Rating text")["City"].value_counts("Restaurant Name")
task_2


# In[9]:


Average_rating = task_2.loc["Average"]
Average_rating.sort_values(ascending=True)


# In[10]:


Average_rating.sort_values(ascending=False)
Average_rating.head(10)


# # THE CITY WITH THE HIGHEST AVERAGE RATING IS NEW DELHI

# # TASK 3

# In[12]:


import matplotlib.pyplot as plt 

x = df["Restaurant Name"].head(50)
y = df["Price range"].head(50)

plt.barh(x,y, height = 0.8)
plt.xlabel("Price Ranges")
plt.ylabel("Names of the Restaurants")
plt.tight_layout()
plt.show()


# In[13]:


x2 = df["Restaurant Name"].tail(50)
y2 = df["Price range"].tail(50)

plt.barh(x2,y2)
plt.xlabel("Price Range")
plt.ylabel("Name of Restaurants")

plt.tight_layout()
plt.show()


# In[43]:


distribution = df.groupby("Price range")["Restaurant Name"].value_counts()
distribution


# In[94]:


pr1 = distribution.loc[1]
result_1 = df["Restaurant Name"].count() / pr1.sum() * 100
result_1


# In[95]:


pr2 = distribution.loc[2]
result_2 = df["Restaurant Name"].count() / pr2.sum() * 100
result_2


# In[96]:


pr3 = distribution.loc[3]
result_3 = df["Restaurant Name"].count() / pr3.sum() * 100
result_3


# In[97]:


pr4 = distribution.iloc[4]
result_4 = df["Restaurant Name"].count() / pr4.sum() * 100
result_4


# # PERCENTAGES OF RESTAURANTS ACCORDING TO THE PRICE RANGES 

# In[98]:


df_1 = print(f'Restaurants with the average 1: {result_1}%')
df_2 = print(f'Restaurants with the average 2: {result_2}%')
df_3 = print(f'Restaurants with the average 3: {result_3}%')
df_4 = print(f'Restaurants with the average 4: {result_4}%')


# # CONCLUDING THAT THE HIGHEST PRICE RANGE IS 4, WHILST THE LOWEST RANGE IS 1

# # TASK 4 

# In[20]:


delivery = df.groupby("Has Online delivery")["Restaurant Name"].describe(include="all")
delivery


# In[21]:


on_delivery = delivery.loc["Yes"]
online_delivery = on_delivery.loc["count"]
online_delivery


# In[22]:


percentage = df["Restaurant Name"].count() / online_delivery * 100
result = print(f'The percentage of restaurants that offer online delivery is: {percentage}%')


# In[7]:


Avg_ratings = df.groupby("Has Online delivery")["Restaurant Name"].value_counts()
Avg_ratings


# In[7]:


Avg_ratings1 = df.groupby("Rating text")["Has Online delivery"].value_counts()
Avg_ratings1


# In[15]:


res = Avg_ratings1.loc["Average"]
res


# In[ ]:




