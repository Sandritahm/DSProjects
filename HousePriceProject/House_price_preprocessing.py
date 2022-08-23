#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import preprocessing


# In[2]:


raw_train = pd.read_csv("train.csv")
prep_train = raw_train.copy()
prep_train.head()


# In[3]:


prep_train.shape


# In[4]:


columns = list(raw_train.columns)
columns


# In[5]:


prep_train[columns[:10]].isnull().sum().to_frame()


# ## Dealing with missing values 
# 
# #### LotFrontage:
# Linear feet of street connected to property
# = I decided to feel out the missing values with the mean, after doing it the describe statistics didn't change too much.

# In[6]:


prep_train['LotFrontage']=prep_train['LotFrontage'].fillna(0)


# #### Alley:
# Type of alley access to property
# The no alley access (NA) was save as a null value, so I just change it to "NA"

# In[7]:


prep_train["Alley"].unique()


# In[8]:


prep_train["Alley"] = prep_train["Alley"].fillna("NA")


# In[9]:


prep_train[columns[:10]].isnull().sum().to_frame()


# In[10]:


prep_train[columns[20:30]].isnull().sum().to_frame()


# #### MasVnrType & MasVnrArea:
# Masonry veneer type & Masonry veneer area in square feet
# 
# Because the rows with missing values are the same. I assume the houses doesn't have a Masonry, so upload to the "None" option.
# For MasVnrArea, upload to zero.

# In[11]:


prep_train["MasVnrType"] = prep_train["MasVnrType"].fillna("None")
prep_train["MasVnrArea"] = prep_train["MasVnrArea"].fillna(0)


# In[12]:


prep_train[columns[20:30]].isnull().sum().to_frame()


# In[13]:


prep_train.shape


# In[14]:


prep_train[columns[30:39]].isnull().sum().to_frame()


# #### Basement
# BsmtQual, BsmtCond, BsmtExposure, BsmtFinType1, BsmtFinType2
# The values are null when there is no basement, so I update to the option "NA" -> No Basement

# In[15]:


prep_train["BsmtQual"].unique()


# In[16]:


prep_train[prep_train['BsmtQual'].isna()]


# In[17]:


prep_train.iloc[17,30:40]


# In[18]:


prep_train["BsmtQual"] = prep_train["BsmtQual"].fillna("NA")
prep_train["BsmtCond"] = prep_train["BsmtCond"].fillna("NA")
prep_train["BsmtExposure"] = prep_train["BsmtExposure"].fillna("NA")
prep_train["BsmtFinType1"] = prep_train["BsmtFinType1"].fillna("NA")
prep_train["BsmtFinType2"] = prep_train["BsmtFinType2"].fillna("NA")


# In[19]:


prep_train[columns[30:39]].isnull().sum().to_frame()


# In[20]:


prep_train[columns[40:]].isnull().sum().to_frame()


# #### Electrical
# 
# Just 1 value missing, so I dropped

# In[21]:


prep_train["Electrical"].unique()


# In[22]:


prep_train = prep_train.dropna(subset=["Electrical"])


# In[23]:


prep_train[columns[40:45]].isnull().sum().to_frame()


# In[24]:


prep_train[columns[56:58]].isnull().sum().to_frame()


# #### Fireplaces
# No fireplace option is presented as null value, so I updated to NA

# In[25]:


prep_train[prep_train['FireplaceQu'].isna()]


# In[26]:


prep_train.iloc[:16,56:58]


# In[27]:


prep_train["FireplaceQu"] = prep_train["FireplaceQu"].fillna("NA")


# In[28]:


prep_train[columns[58:66]].isnull().sum().to_frame()


# #### Garage
# 
# 
# When is no garage the value is null value, so I updated to NA

# In[29]:


prep_train[prep_train['GarageType'].isna()]


# In[30]:


prep_train.iloc[39:49,58:65]


# In[31]:


prep_train["GarageType"] = prep_train["GarageType"].fillna("NA")
prep_train["GarageFinish"] = prep_train["GarageFinish"].fillna("NA")
prep_train["GarageQual"] = prep_train["GarageQual"].fillna("NA")
prep_train["GarageCond"] = prep_train["GarageCond"].fillna("NA")
prep_train["GarageYrBlt"] = prep_train["GarageYrBlt"].fillna(0)


# In[32]:


prep_train[columns[71:]].isnull().sum().to_frame()


# #### Pool & Fence

# In[33]:


prep_train["PoolQC"] = prep_train["PoolQC"].fillna("NA")
prep_train["Fence"] = prep_train["Fence"].fillna("NA")
prep_train["MiscFeature"] = prep_train["MiscFeature"].fillna("NA")


# In[34]:


y_train = prep_train["SalePrice"]
prep_train = prep_train.drop(["Id","SalePrice"], axis=1)


# Getting dummies from data:

# In[35]:


data_dummies = pd.get_dummies(prep_train, drop_first=True)
data_dummies.head()


# In[36]:


columns = list(data_dummies.columns)
columns


# In[37]:


unscaled_inputs_all = data_dummies.drop(['Utilities_NoSeWa',
 'Condition2_RRAe',
 'Condition2_RRAn',
 'Condition2_RRNn',
 'HouseStyle_2.5Fin',
 'RoofMatl_CompShg',
 'RoofMatl_Membran',
 'RoofMatl_Metal',
 'RoofMatl_Roll',
 'Exterior1st_ImStucc',
 'Exterior1st_Stone',
 'Exterior2nd_Other',
 'Heating_GasA',
 'Heating_OthW',
 'Electrical_Mix',
 'GarageQual_Fa',
 'PoolQC_Fa',
 'MiscFeature_TenC'], axis=1)

targets_all = y_train


# In[38]:


unscaled_inputs_all.shape


# Standardize Inputs

# In[39]:


scaled_inputs = preprocessing.scale(unscaled_inputs_all)
scaled_inputs.shape


# In[40]:


scaled_inputs


# Splitting datasets

# In[41]:


samples_count = scaled_inputs.shape[0]

# Count the samples in each subset, assuming we want 80-10-10 distribution of training, validation, and test.
train_samples_count = int(0.8 * samples_count)
validation_samples_count = int(0.1 * samples_count)

# The 'test' dataset contains all remaining data.
test_samples_count = samples_count - train_samples_count - validation_samples_count

# Create variables that record the inputs and targets for training
train_inputs = scaled_inputs[:train_samples_count]
train_targets = targets_all[:train_samples_count]

# Create variables that record the inputs and targets for validation.
validation_inputs = scaled_inputs[train_samples_count:train_samples_count+validation_samples_count]
validation_targets = targets_all[train_samples_count:train_samples_count+validation_samples_count]

# Create variables that record the inputs and targets for test.
test_inputs = scaled_inputs[train_samples_count+validation_samples_count:]
test_targets = targets_all[train_samples_count+validation_samples_count:]

print(np.sum(train_targets), train_samples_count, np.sum(train_targets) / train_samples_count)
print(np.sum(validation_targets), validation_samples_count, np.sum(validation_targets) / validation_samples_count)
print(np.sum(test_targets), test_samples_count, np.sum(test_targets) / test_samples_count)


# In[42]:


np.savez('HousePrice_data_train', inputs=train_inputs, targets=train_targets)
np.savez('HousePrices_data_validation', inputs=validation_inputs, targets=validation_targets)
np.savez('HousePrice_data_test', inputs=test_inputs, targets=test_targets)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




