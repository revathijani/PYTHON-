#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[6]:


data=pd.read_csv('udemy_courses.csv',parse_dates=['published_timestamp'])


# In[8]:


data.dtypes


# # 1. Display Top 10 Rows of The Dataset

# In[9]:


data.head(10)


# # 2. Check Last 5 Rows of The Dataset

# In[10]:


data.tail()


# # 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)

# In[11]:


data.shape


# In[12]:


print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])


# # 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

# In[13]:


data.info()


# # 5. Check Null Values In The Dataset

# In[14]:


data.isnull().sum()


# In[15]:


print("Any Missing Value?",data.isnull().values.any())


# In[18]:


sns.heatmap(data.isnull())


# # 6. Check For Duplicate Data and Drop Them

# In[19]:


dup=data.duplicated().any()


# In[20]:


print("Are There any duplicated in data",dup)


# In[21]:


data=data.drop_duplicates()


# In[22]:


dup=data.duplicated().any()
print("Are There any duplicated in data",dup)


# # 7. Find Out Number of Courses Per Subjects
# 

# In[23]:


data.columns


# In[25]:


data.groupby('subject')['course_id'].count().sort_values(ascending=False)


# In[26]:


data['subject'].value_counts()


# In[27]:


import matplotlib.pyplot as plt


# In[28]:


sns.countplot(data['subject'])
plt.xlabel("Subjects",fontsize=13)
plt.ylabel("Number of Courses per subject",fontsize=13)
plt.xticks(rotation=65)
plt.show()


# # 8. For Which Levels, Udemy Courses Providing The Courses

# In[29]:


data.columns


# In[30]:


data['level'].value_counts()


# In[31]:


sns.countplot(data['level'])
plt.xlabel("Level",fontsize=13)
plt.ylabel("Number of Courses per level",fontsize=13)
plt.xticks(rotation=65)
plt.show()


# # 9. Display The Count of Paid and Free Courses
# 

# In[32]:


data.columns


# In[33]:


data['is_paid'].value_counts()


# In[34]:


sns.countplot(data['is_paid'])
plt.xlabel("Level",fontsize=13)
plt.ylabel("Number of Free And Paid Courses",fontsize=13)
plt.xticks(rotation=65)
plt.show()


# # 10. Which Course Has More Lectures (Free or Paid)?

# In[35]:


data.groupby(['is_paid']).mean()


# # 11. Which Courses Have A Higher Number of Subscribers Free or Paid?

# In[36]:


data.columns


# In[39]:


sns.barplot(x="is_paid",y="num_subscribers",data=data)


# # 12. Which Level Has The Highest Number of Subscribers?

# In[40]:


data.columns


# In[42]:


sns.barplot(x="level",y="num_subscribers",data=data)
plt.xticks(rotation=60)
plt.show()


# # 13. Find Most Popular Course Title

# In[43]:


data.columns


# In[44]:


data[data['num_subscribers'].max()==data['num_subscribers']]['course_title']


# # 14. Display 10 Most Popular Courses As Per Number of Subscribers

# In[47]:


top_10=data.sort_values(by="num_subscribers",ascending=False).head(10)


# In[48]:


sns.barplot(x="num_subscribers",y="course_title",data=top_10)


# # 15. Find The Course Which Is Having The Highest Number of Reviews.

# In[49]:


data.columns


# In[50]:


plt.figure(figsize=(10,4))
sns.barplot(x="subject",y="num_reviews",data=data)


# # 16. Does Price Affect Number of Reviews?

# In[51]:


plt.figure(figsize=(15,6))
sns.scatterplot(x="price",y="num_reviews",data=data)


# # 17. Find Total Number of Courses Related To Python

# In[52]:


data.columns


# In[55]:


len(data[data['course_title'].str.contains('python',case=False)])


# # 18. Display 10 Most Popular Python Courses As Per Number of Subscribers

# In[56]:


python=data[data['course_title'].str.contains('python',case=False)].sort_values(by="num_subscribers",ascending=False).head(10)


# In[57]:


sns.barplot(x="num_subscribers",y="course_title",data=python)


# # 19. In Which Year The Highest Number of Courses Were Posted?

# In[58]:


data.columns


# In[59]:


data['Year']=data['published_timestamp'].dt.year


# In[60]:


data.head(1)


# In[61]:


sns.countplot('Year',data=data)


# # 20. Display Category-Wise Count of Posted Subjects [Year Wise]

# In[62]:


data.groupby('Year')['subject'].value_counts()


# In[ ]:




