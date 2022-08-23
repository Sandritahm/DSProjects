#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


npz = np.load('HousePrice_data_train.npz')

train_inputs = npz['inputs'].astype(float)
train_targets = npz['targets'].astype(int)

npz = np.load('HousePrices_data_validation.npz')
validation_inputs, validation_targets = npz['inputs'].astype(float), npz['targets'].astype(int)

npz = np.load('HousePrice_data_test.npz')
test_inputs, test_targets = npz['inputs'].astype(float), npz['targets'].astype(int)


# In[3]:


train_inputs.shape


# NN model

# In[4]:


# Set the input and output sizes
input_size = 241
output_size = 1
# Use same hidden layer size for both hidden layers. Not a necessity.
hidden_layer_size = 128
    
# define how the model will look like
model = tf.keras.Sequential([
    tf.keras.layers.Dense(hidden_layer_size, activation='relu'), # 1st hidden layer
    tf.keras.layers.Dense(hidden_layer_size, activation='relu'), # 2nd hidden layer
    tf.keras.layers.Dense(hidden_layer_size, activation='relu'), # 3nd hidden layer
    tf.keras.layers.Dense(output_size) # output layer
])


model.compile(optimizer='adam', loss='mean_squared_error', metrics='mean_squared_error')

batch_size = 100
max_epochs = 1000
early_stopping = tf.keras.callbacks.EarlyStopping(patience=10)

model.fit(train_inputs, # train inputs
          train_targets, # train targets
          batch_size=batch_size, # batch size
          epochs=max_epochs, # epochs that we will train for (assuming early stopping doesn't kick in)
          callbacks=[early_stopping], # early stopping
          validation_data=(validation_inputs, validation_targets), # validation data
          verbose = 2 # making sure we get enough information about the training process
          )  


# In[5]:


y_pred = model.predict(test_inputs)
df_pf = pd.DataFrame(model.predict(test_inputs), columns=['Prediction'])
y_test = pd.Series(test_targets).reset_index(drop=True)
df_pf['Target'] = y_test
df_pf['Residual'] = df_pf['Target'] - df_pf['Prediction']
df_pf['Difference%'] = np.absolute(df_pf['Residual']/df_pf['Target']*100)
df_pf


# In[6]:


plt.plot(y_test, color = 'red', label = 'Real data')
plt.plot(y_pred, color = 'blue', label = 'Predicted data')
plt.title('Prediction')
plt.legend()
plt.show()


# In[7]:


print("Accuracy =", round(100-np.mean(df_pf['Difference%']), 2))


# # Prediction Test Data

# In[8]:


pred = np.load('HousePrice_data_test_predictions.npz')
pred_inputs = pred['inputs'].astype(float)
pred_ids = pred['ids'].astype(int)


# In[9]:


#y_prediction_testing = model.predict(pred_inputs)

#df_pf = pd.DataFrame(pred_ids, columns=['Id'])
#df_pf['SalePrice'] = model.predict(pred_inputs)
#df_pf


# In[10]:


ids = pd.Series(pred_ids).reset_index(drop=True)


# In[13]:


y_pred = model.predict(pred_inputs)

df_pf = pd.DataFrame(pred_ids, columns=['Id'])
df_pf['SalePrice'] = model.predict(pred_inputs)

#df_pf = pd.DataFrame(model.predict(pred_inputs), columns=['SalePrice'])
#df_pf['Id'] = ids
df_pf


# In[14]:


df_pf.to_csv("Predictions_sd.csv", index=False)


# In[ ]:




