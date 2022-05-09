#!/usr/bin/env python
# coding: utf-8

# In[63]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

#importing the dataset and data cleaning

#Function to split dataset into two parts. One for training, one for testing
#Code for this function was found on StackExchange
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


og_data = pd.read_csv("https://raw.githubusercontent.com/kasterlevi/CSE543_NBA_Project/main/NBA_Player_StatsV2.csv")
og_data = og_data.dropna()
og_train_data, og_test_data = split_train_test(og_data, 0.2)


target_pts_train = og_train_data.iloc[:, 30] # target training variable: points scored
target_trb_train = og_train_data.iloc[:, 31]  # target training variable: total rebounds
target_ast_train = og_train_data.iloc[:, 32]  # target training variable: total assists
train_data = og_train_data.iloc[:, 5:29]  # Matrix of training data

target_pts_test = og_test_data.iloc[:, 30]  # target training variable: points scored
target_trb_test = og_test_data.iloc[:, 31]    # target training variable: total rebounds
target_ast_test = og_test_data.iloc[:, 32]  # target training variable: total assists
test_data = og_test_data.iloc[:, 5:29]  # Matrix of training data

scaler = preprocessing.MinMaxScaler().fit(train_data)  #set teh scaler
train_data_scaled = scaler.transform(train_data) #scale training data
test_data_scaled = scaler.transform(test_data) #scale test data
regr = MLPRegressor(random_state=1, max_iter=10000).fit(train_data_scaled, target_pts_train)  # fit training data
regr.predict(test_data_scaled)   #predict test data
regr.score(test_data_scaled, target_pts_test)  #r score of points scored
regr.score(test_data_scaled, target_trb_test)  #r score of total rebounds
regr.score(test_data_scaled, target_ast_test)  #r score of total assists


# In[ ]:





# In[ ]:





# In[ ]:




