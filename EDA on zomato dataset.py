#!/usr/bin/env python
# coding: utf-8

# ### EDA ON ZOMATO DATASET 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("C:/Users/saiku/Downloads/Zomatodataset/zomato.csv",encoding = 'latin-1')
df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# ## Things to do in Data Analysis
# 1. missing values
# 2. explore about numerical variables
# 3. explore about categorical variables
# 4. finding relationship between features

# In[5]:


df.isnull().sum()


# In[6]:


[features for features in df.columns if df[features].isnull().sum()>1]


# In[7]:


df_country = pd.read_excel("C:/Users/saiku/Downloads/Zomatodataset/Country-Code.xlsx")


# In[8]:


df_country.head()


# In[9]:


df.columns


# In[10]:


final_df = pd.merge(df,df_country, on = 'Country Code', how = 'left')
final_df.head(2)


# In[11]:


final_df.dtypes


# In[12]:


country_names = final_df.Country.value_counts().index


# In[13]:


country_val = final_df.Country.value_counts().values
country_val


# In[14]:


plt.pie(country_val[:3],labels = country_names[:3],autopct='%1.2f%%')


# # observations
# 1. india is more popular,next comes united states followed by united kingdom

# In[15]:


final_df.columns


# In[16]:


ratings = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[17]:


ratings


# ## observation
# 1. when rating is between 4.5 to 4.9 refers to excellent
# 2. when rating is between 4.0 to 4.4 refers to very good
# 3. when rating is between 3.5 to 3.9 refers t0 good
# 4. when rating is between 2.5 to 3.4 refers to average
# 5. when rating is between 1.8 to 2.4 refters to poor

# In[18]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x ='Aggregate rating',y = 'Rating Count',data = ratings)


# In[19]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x ='Aggregate rating',y = 'Rating Count',hue ='Rating color',data = ratings,palette = ['black','red','orange','yellow','green','green'])


# ### Observation
# 1 . Not rated count is very high
# 
# 2 . Maximum number of rating are between 2.5 to 3.4

# In[20]:


##
sns.countplot(x = 'Rating color',data = ratings,palette = ['blue','red','orange','yellow','green','green'])


# In[21]:


### Find the countries name that has given 0 rating
final_df[final_df['Rating color'] =='White'].groupby('Country').size().reset_index()


# In[22]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head()


# ### OBSERVATIONS
# Maximum number of 0 ratings are from indian customers

# In[23]:


## Find out which currency is used by which country?
final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[24]:


## which country do have online delivery?
final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# ## observation
# 
# 1.online deliveries are available in india and UAE

# In[25]:


final_df.columns


# In[26]:


## create a pie chart for top 5 cities distribution
final_df.City.value_counts().index


# In[27]:


city_values = final_df.City.value_counts().values
city_labels = final_df.City.value_counts().index


# In[28]:


plt.pie(city_values[:5],labels = city_labels[:5],autopct ='%1.2f%%')


# In[29]:


## find top 10 cuisine
final_df[['Cuisines','Votes']].groupby(['Cuisines','Votes']).size().reset_index()


# In[ ]:




