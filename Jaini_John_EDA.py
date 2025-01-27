#!/usr/bin/env python
# coding: utf-8

# ## Exploratory Data Analysis

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Load datasets
customers = pd.read_csv('/Users/jaini/Downloads/Customers.csv')
products = pd.read_csv('/Users/jaini/Downloads/Products.csv')
transactions = pd.read_csv('/Users/jaini/Downloads/Transactions.csv')


# ### Check dataset structure

# In[3]:


customers.head()


# In[4]:


customers.info()


# In[5]:


products.head()


# In[6]:


products.info()


# In[7]:


transactions.head()


# In[8]:


transactions.info()


# ### Data cleaning

# #### Check for Missing Values:

# In[9]:


customers.isnull().sum()


# In[10]:


products.isnull().sum()


# In[11]:


transactions.isnull().sum()


# No missing values present in the dataset

# #### Handle Duplicates:

# In[12]:


customers.duplicated().sum()


# In[13]:


products.duplicated().sum()


# In[14]:


transactions.duplicated().sum()


# No duplicates found

# #### Convert Datatype

# In[15]:


#coverting from object datatype to datetime
customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])


# In[16]:


# Verify changes
print(customers.dtypes)
print(transactions.dtypes)


# #### Analysis

# In[17]:


# Count customers by region
region_counts = customers['Region'].value_counts()
print(region_counts)

# Plot regional distribution
region_counts.plot(kind='bar', title='Customer Distribution by Region')
plt.xlabel('Region')
plt.ylabel('Number of Customers')
plt.show()


# In[18]:


# Count products by category
category_counts = products['Category'].value_counts()
print(category_counts)

# Plot product category distribution
category_counts.plot(kind='pie', autopct='%1.1f%%', title='Product Distribution by Category')
plt.show()


# In[19]:


# Distribution of total transaction values
transactions['TotalValue'].plot(kind='hist', bins=50, title='Distribution of Transaction Values')
plt.xlabel('Transaction Value (USD)')
plt.show()


# #### Multivariate Analysis

# In[20]:


customers['SignupYear'] = customers['SignupDate'].dt.year
signup_trends = customers.groupby('SignupYear').size()
signup_trends.plot(kind='line', title='Customer Signups Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Signups')
plt.show()


# In[21]:


# Merge transactions with products
transactions_products = pd.merge(transactions, products, on='ProductID')

# Calculate total sales by product
product_sales = transactions_products.groupby('ProductName')['TotalValue'].sum().sort_values(ascending=False)
print(product_sales.head(10))

# Plot top 10 products
product_sales.head(10).plot(kind='bar', title='Top 10 Products by Sales')
plt.xlabel('Product Name')
plt.ylabel('Total Sales (USD)')
plt.show()


# In[22]:


# Merge transactions with customers
transactions_customers = pd.merge(transactions, customers, on='CustomerID')

# Calculate sales by region
regional_sales = transactions_customers.groupby('Region')['TotalValue'].sum()
print(regional_sales)

# Plot regional sales
regional_sales.plot(kind='bar', title='Sales Performance by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales (USD)')
plt.show()


# In[ ]:




