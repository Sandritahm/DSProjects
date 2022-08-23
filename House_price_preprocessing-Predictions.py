#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from sklearn import preprocessing


# Test data

# In[2]:


raw_test = pd.read_csv("test.csv")
prep_test = raw_test.copy()
prep_test


# In[3]:


columns_1 = list(raw_test.columns)
columns_1


# In[4]:


prep_test[columns_1[60:]].isnull().sum().to_frame()


# In[5]:


prep_test["GarageArea"].value_counts()


# In[6]:


#prep_test = prep_test.dropna(subset=[
   # "MSZoning",
   # "Utilities",
   # "Exterior1st",
   # "BsmtFinSF1",
   # "BsmtFullBath",
   # "KitchenQual",
   # "Functional",
   # "GarageCars",
   # "SaleType"
#])


# I add the missing value to the most common

# In[7]:


prep_test["MSZoning"] = prep_test["MSZoning"].fillna("RL")
prep_test["Utilities"] = prep_test["Utilities"].fillna("AllPub")
prep_test["Exterior1st"] = prep_test["Exterior1st"].fillna("VinylSd")
prep_test["BsmtFinSF1"] = prep_test["BsmtFinSF1"].fillna(0.0)
prep_test["BsmtFullBath"] = prep_test["BsmtFullBath"].fillna(0.0)
prep_test["KitchenQual"] = prep_test["KitchenQual"].fillna("TA")
prep_test["Functional"] = prep_test["Functional"].fillna("Typ")
prep_test["GarageCars"] = prep_test["GarageCars"].fillna(2.0)
prep_test["SaleType"] = prep_test["SaleType"].fillna("WD")
prep_test["BsmtFinSF2"] = prep_test["BsmtFinSF2"].fillna(0.0)
prep_test["BsmtUnfSF"] = prep_test["BsmtUnfSF"].fillna(0.0)
prep_test["TotalBsmtSF"] = prep_test["TotalBsmtSF"].fillna(0.0)
prep_test["GarageArea"] = prep_test["GarageArea"].fillna(0.0)


# In[8]:


prep_test['LotFrontage'] = prep_test['LotFrontage'].fillna(0)
prep_test['MasVnrArea'] = prep_test['MasVnrArea'].fillna(0)
prep_test['GarageYrBlt'] = prep_test['GarageYrBlt'].fillna(0)


# In[9]:


prep_test["Alley"] = prep_test["Alley"].fillna("NA")
prep_test["BsmtQual"] = prep_test["BsmtQual"].fillna("NA")
prep_test["BsmtCond"] = prep_test["BsmtCond"].fillna("NA")
prep_test["BsmtExposure"] = prep_test["BsmtExposure"].fillna("NA")
prep_test["BsmtFinType1"] = prep_test["BsmtFinType1"].fillna("NA")
prep_test["BsmtFinType2"] = prep_test["BsmtFinType2"].fillna("NA")
prep_test["FireplaceQu"] = prep_test["FireplaceQu"].fillna("NA")
prep_test["GarageType"] = prep_test["GarageType"].fillna("NA")
prep_test["GarageFinish"] = prep_test["GarageFinish"].fillna("NA")
prep_test["GarageQual"] = prep_test["GarageQual"].fillna("NA")
prep_test["GarageCond"] = prep_test["GarageCond"].fillna("NA")
prep_test["PoolQC"] = prep_test["PoolQC"].fillna("NA")
prep_test["Fence"] = prep_test["Fence"].fillna("NA")
prep_test["MiscFeature"] = prep_test["MiscFeature"].fillna("NA")

prep_test["MasVnrType"] = prep_test["MasVnrType"].fillna("None")


# In[10]:


ids = prep_test["Id"]
prep_test = prep_test.drop(["Id"], axis=1)


# In[11]:


data_dummies = pd.get_dummies(prep_test, drop_first=True)
data_dummies.shape


# In[12]:


columns_test = list(data_dummies.columns)
columns_test


# In[13]:


columns_train = ['MSSubClass',
 'LotFrontage',
 'LotArea',
 'OverallQual',
 'OverallCond',
 'YearBuilt',
 'YearRemodAdd',
 'MasVnrArea',
 'BsmtFinSF1',
 'BsmtFinSF2',
 'BsmtUnfSF',
 'TotalBsmtSF',
 '1stFlrSF',
 '2ndFlrSF',
 'LowQualFinSF',
 'GrLivArea',
 'BsmtFullBath',
 'BsmtHalfBath',
 'FullBath',
 'HalfBath',
 'BedroomAbvGr',
 'KitchenAbvGr',
 'TotRmsAbvGrd',
 'Fireplaces',
 'GarageYrBlt',
 'GarageCars',
 'GarageArea',
 'WoodDeckSF',
 'OpenPorchSF',
 'EnclosedPorch',
 '3SsnPorch',
 'ScreenPorch',
 'PoolArea',
 'MiscVal',
 'MoSold',
 'YrSold',
 'MSZoning_FV',
 'MSZoning_RH',
 'MSZoning_RL',
 'MSZoning_RM',
 'Street_Pave',
 'Alley_NA',
 'Alley_Pave',
 'LotShape_IR2',
 'LotShape_IR3',
 'LotShape_Reg',
 'LandContour_HLS',
 'LandContour_Low',
 'LandContour_Lvl',
 'Utilities_NoSeWa',
 'LotConfig_CulDSac',
 'LotConfig_FR2',
 'LotConfig_FR3',
 'LotConfig_Inside',
 'LandSlope_Mod',
 'LandSlope_Sev',
 'Neighborhood_Blueste',
 'Neighborhood_BrDale',
 'Neighborhood_BrkSide',
 'Neighborhood_ClearCr',
 'Neighborhood_CollgCr',
 'Neighborhood_Crawfor',
 'Neighborhood_Edwards',
 'Neighborhood_Gilbert',
 'Neighborhood_IDOTRR',
 'Neighborhood_MeadowV',
 'Neighborhood_Mitchel',
 'Neighborhood_NAmes',
 'Neighborhood_NPkVill',
 'Neighborhood_NWAmes',
 'Neighborhood_NoRidge',
 'Neighborhood_NridgHt',
 'Neighborhood_OldTown',
 'Neighborhood_SWISU',
 'Neighborhood_Sawyer',
 'Neighborhood_SawyerW',
 'Neighborhood_Somerst',
 'Neighborhood_StoneBr',
 'Neighborhood_Timber',
 'Neighborhood_Veenker',
 'Condition1_Feedr',
 'Condition1_Norm',
 'Condition1_PosA',
 'Condition1_PosN',
 'Condition1_RRAe',
 'Condition1_RRAn',
 'Condition1_RRNe',
 'Condition1_RRNn',
 'Condition2_Feedr',
 'Condition2_Norm',
 'Condition2_PosA',
 'Condition2_PosN',
 'Condition2_RRAe',
 'Condition2_RRAn',
 'Condition2_RRNn',
 'BldgType_2fmCon',
 'BldgType_Duplex',
 'BldgType_Twnhs',
 'BldgType_TwnhsE',
 'HouseStyle_1.5Unf',
 'HouseStyle_1Story',
 'HouseStyle_2.5Fin',
 'HouseStyle_2.5Unf',
 'HouseStyle_2Story',
 'HouseStyle_SFoyer',
 'HouseStyle_SLvl',
 'RoofStyle_Gable',
 'RoofStyle_Gambrel',
 'RoofStyle_Hip',
 'RoofStyle_Mansard',
 'RoofStyle_Shed',
 'RoofMatl_CompShg',
 'RoofMatl_Membran',
 'RoofMatl_Metal',
 'RoofMatl_Roll',
 'RoofMatl_Tar&Grv',
 'RoofMatl_WdShake',
 'RoofMatl_WdShngl',
 'Exterior1st_AsphShn',
 'Exterior1st_BrkComm',
 'Exterior1st_BrkFace',
 'Exterior1st_CBlock',
 'Exterior1st_CemntBd',
 'Exterior1st_HdBoard',
 'Exterior1st_ImStucc',
 'Exterior1st_MetalSd',
 'Exterior1st_Plywood',
 'Exterior1st_Stone',
 'Exterior1st_Stucco',
 'Exterior1st_VinylSd',
 'Exterior1st_Wd Sdng',
 'Exterior1st_WdShing',
 'Exterior2nd_AsphShn',
 'Exterior2nd_Brk Cmn',
 'Exterior2nd_BrkFace',
 'Exterior2nd_CBlock',
 'Exterior2nd_CmentBd',
 'Exterior2nd_HdBoard',
 'Exterior2nd_ImStucc',
 'Exterior2nd_MetalSd',
 'Exterior2nd_Other',
 'Exterior2nd_Plywood',
 'Exterior2nd_Stone',
 'Exterior2nd_Stucco',
 'Exterior2nd_VinylSd',
 'Exterior2nd_Wd Sdng',
 'Exterior2nd_Wd Shng',
 'MasVnrType_BrkFace',
 'MasVnrType_None',
 'MasVnrType_Stone',
 'ExterQual_Fa',
 'ExterQual_Gd',
 'ExterQual_TA',
 'ExterCond_Fa',
 'ExterCond_Gd',
 'ExterCond_Po',
 'ExterCond_TA',
 'Foundation_CBlock',
 'Foundation_PConc',
 'Foundation_Slab',
 'Foundation_Stone',
 'Foundation_Wood',
 'BsmtQual_Fa',
 'BsmtQual_Gd',
 'BsmtQual_NA',
 'BsmtQual_TA',
 'BsmtCond_Gd',
 'BsmtCond_NA',
 'BsmtCond_Po',
 'BsmtCond_TA',
 'BsmtExposure_Gd',
 'BsmtExposure_Mn',
 'BsmtExposure_NA',
 'BsmtExposure_No',
 'BsmtFinType1_BLQ',
 'BsmtFinType1_GLQ',
 'BsmtFinType1_LwQ',
 'BsmtFinType1_NA',
 'BsmtFinType1_Rec',
 'BsmtFinType1_Unf',
 'BsmtFinType2_BLQ',
 'BsmtFinType2_GLQ',
 'BsmtFinType2_LwQ',
 'BsmtFinType2_NA',
 'BsmtFinType2_Rec',
 'BsmtFinType2_Unf',
 'Heating_GasA',
 'Heating_GasW',
 'Heating_Grav',
 'Heating_OthW',
 'Heating_Wall',
 'HeatingQC_Fa',
 'HeatingQC_Gd',
 'HeatingQC_Po',
 'HeatingQC_TA',
 'CentralAir_Y',
 'Electrical_FuseF',
 'Electrical_FuseP',
 'Electrical_Mix',
 'Electrical_SBrkr',
 'KitchenQual_Fa',
 'KitchenQual_Gd',
 'KitchenQual_TA',
 'Functional_Maj2',
 'Functional_Min1',
 'Functional_Min2',
 'Functional_Mod',
 'Functional_Sev',
 'Functional_Typ',
 'FireplaceQu_Fa',
 'FireplaceQu_Gd',
 'FireplaceQu_NA',
 'FireplaceQu_Po',
 'FireplaceQu_TA',
 'GarageType_Attchd',
 'GarageType_Basment',
 'GarageType_BuiltIn',
 'GarageType_CarPort',
 'GarageType_Detchd',
 'GarageType_NA',
 'GarageFinish_NA',
 'GarageFinish_RFn',
 'GarageFinish_Unf',
 'GarageQual_Fa',
 'GarageQual_Gd',
 'GarageQual_NA',
 'GarageQual_Po',
 'GarageQual_TA',
 'GarageCond_Fa',
 'GarageCond_Gd',
 'GarageCond_NA',
 'GarageCond_Po',
 'GarageCond_TA',
 'PavedDrive_P',
 'PavedDrive_Y',
 'PoolQC_Fa',
 'PoolQC_Gd',
 'PoolQC_NA',
 'Fence_GdWo',
 'Fence_MnPrv',
 'Fence_MnWw',
 'Fence_NA',
 'MiscFeature_NA',
 'MiscFeature_Othr',
 'MiscFeature_Shed',
 'MiscFeature_TenC',
 'SaleType_CWD',
 'SaleType_Con',
 'SaleType_ConLD',
 'SaleType_ConLI',
 'SaleType_ConLw',
 'SaleType_New',
 'SaleType_Oth',
 'SaleType_WD',
 'SaleCondition_AdjLand',
 'SaleCondition_Alloca',
 'SaleCondition_Family',
 'SaleCondition_Normal',
 'SaleCondition_Partial']



# In[14]:


missing = []
column_no = []

for x in columns_train:
    if x not in columns_test:
        missing.append(x)
        
missing


# In[ ]:





# In[15]:


scaled_inputs = preprocessing.scale(data_dummies)
scaled_inputs.shape


# In[16]:


np.savez('HousePrice_data_test_predictions', inputs=scaled_inputs, ids=ids)


# In[ ]:





# In[ ]:




