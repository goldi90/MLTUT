#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[1]:


# single dimension= series object
# multi dimension = dataframe


# ## Series

# In[2]:


# series object
import pandas as pd
PArray=pd.Series([1,2,3,4,5])
PArray
# Here 0 is index of 1 and so on


# In[3]:


type(PArray)


# In[4]:


# changing index
Changing_Index=pd.Series([5,7,6,5,2,3,2],index=["A","B","C","D","E","F","G"])
Changing_Index


# In[5]:


# series with dictoniries
STdictoniries=pd.Series({"A":1,"B":2,"C":3,"D":4})
print(STdictoniries)


# In[6]:


# series with dictoniries change index
STdictoniriesCI=pd.Series({"A":1,"B":2,"C":3,"D":4},index=["A","B","D","E"])
print(STdictoniriesCI)


# In[7]:


# extracting  Single Element
SimpleSeriesOfPD=pd.Series([1,5,7,93,5,41,5,6,9,7])
SimpleSeriesOfPD[3]


# In[8]:


SimpleSeriesOfPD[-3:]


# In[9]:


SimpleSeriesOfPD[:4]


# In[10]:


# math operation on series
# Sum
MathSeries=pd.Series([10,50,78,62,41])
MathSeries+3


# In[11]:


#Sub
MathSeries-3


# In[12]:


# divide
MathSeries/10


# In[13]:


# Ading two Series
SeriesOne=pd.Series([14,75,35,41,85,32,41,62,30])
SeriesTwo=pd.Series([51,65,72,68,15,32,15,17,86])
SeriesOne+SeriesTwo


# ## Data frame

# In[15]:


# creating Daa frame using dictinories
DataFrame=pd.DataFrame({"Name":["kaushik","Harsh","Abhinesh","Reena"],"ID":[101,102,103,104]})
print(DataFrame)


# In[17]:


# dataframe Bulitin function
# 1)head() to get first five rows in data set
# 2)describe() to get general information abut data aset
# 3)tail() to get last five rows in data set
# 4)shape() to get rows and colum in dat set


# In[21]:


# load dataset
iris=pd.read_csv('iris.csv')


# In[22]:


# first five record of data set
iris.head()


# In[24]:


iris.tail()


# In[25]:


iris.describe()


# In[27]:


iris.shape


# In[34]:


# iloc[rows,colums] to extract value from data set using index
iris.iloc[5:11,2:]


# In[38]:


# loc[colums names] to extract value from data set using colum names
iris.loc[0:3,("SepalWidthCm","PetalLengthCm","Species")] # here 0:3 is rows and both inclusive


# In[40]:


iris.head()


# In[42]:


# Droping colums
iris.drop("PetalWidthCm",axis=1) # 1= drop column and 0 = drop rows


# In[45]:



# droping rows 
# iris.drop([index of rows],axis=0)
iris.drop([1,2,3],axis=0)


# In[46]:


# dat aset mean median min max
iris.mean()


# In[48]:


iris.median()


# In[49]:


iris.max()


# In[50]:


iris.min()


# In[58]:


# apply  function . user defined function apply on dat aset or its cloums "half is user define function"
def double_make(s):
    return s*2


# In[59]:


iris.head()


# In[60]:


iris[["PetalWidthCm","PetalLengthCm"]].apply(double_make)


# In[ ]:


# value count
# sort values


# In[62]:


iris["Species"].value_counts()


# In[63]:


iris.sort_values(by="SepalWidthCm")

