from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#This file performs the Random Forest Regression

#Function to split dataset into two parts. One for training, one for testing
#Code for this function was found on StackExchange
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


#This function performs the random forest regression
# input: n_trees - the number of trees to be used in the random forest
# output: oob_error - the out of bag error for the random forest
# the training and testing errors and R-squared values are also calculated
def model(n_trees):
    og_data = pd.read_csv(
                 'NBA_Player_StatsV2.csv')
    og_data = og_data.dropna()
    og_train_data, og_test_data = split_train_test(og_data, 0.2)

    target_pts_train = og_train_data.iloc[:, 30] # target training variable: points scored
    target_trb_train = og_train_data.iloc[:, 31] # target training variable: total rebounds
    target_ast_train = og_train_data.iloc[:, 32] # target training variable: total assists
    train_data = og_train_data.iloc[:, 5:29] # Matrix of training data


    target_pts_test = og_test_data.iloc[:, 30] # target testing variable: points scored
    target_trb_test = og_test_data.iloc[:, 31] # target testing variable: total rebounds
    target_ast_test = og_test_data.iloc[:, 32] # target testing variable: total assists
    test_data = og_test_data.iloc[:, 5:29] # Matrix of testing data

    rff = RandomForestRegressor(n_estimators=n_trees, oob_score=True)
    rff = rff.fit(train_data, target_ast_train) # fit training data
    train_pred = rff.predict(train_data) # training predictions
    test_pred = rff.predict(test_data) # testing predictions

    R_sq_train = rff.score(train_data, target_ast_train) # training R-squared score
    R_sq_test = rff.score(test_data, target_ast_test) # testing R-squared score
    # Calculation of training error
    train_error = 0
    for i in range(len(target_ast_train)):
        train_error = train_error+(train_pred[i] -
                                   target_ast_train.iloc[i])**2
    train_error = train_error/len(target_ast_train)
    # Calculation of testing error
    test_error = 0
    for i in range(len(target_ast_test)):
        test_error = test_error+(test_pred[i] - target_ast_test.iloc[i])**2
    test_error = test_error/len(target_ast_test)
    
    oob_error = rff.oob_score_ # Out-of-bag error
    print(train_error)
    print(test_error)
    print(R_sq_train)
    print(R_sq_test)
    print(oob_error)
    return oob_error

#main function runs the random forest regression by calling the model() function for various forest sizes and plots the results
def main():
    trees_array = np.arange(100, 300)
    oob_error_arr = np.zeros(199)
    for i in range(len(trees_array)):
        oob_error_arr[i] = model(trees_array[i])
    plt.plot(trees_array, oob_error_arr, label="oob error")
    plt.title("OOB error per number of trees (Assists)")
    plt.xlabel("Number of Trees")
    plt.ylabel("Error")
    plt.show()


if __name__ == "__main__":
    main()
