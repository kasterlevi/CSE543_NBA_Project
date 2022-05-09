# CSE543_NBA_Project
Software Package for the CSE 543T project with Yang Yi, Levi Kaster, Allen Huang, and Patrick Norrick.

In this project we testest 5 different regression models for predicting the single-season points, rebounds, and assists of NBA Players. The models we tested were a kNN Regression model, a Linear Regression Model, A Random Forest Model, and a Deep Neural Network.

# Duplication of Results 

1. [NBA_Player_CSV](https://github.com/kasterlevi/CSE543_NBA_Project/blob/main/NBA_Player_CSV.ipynb): This file gives the code necessary for obtaining the data that we used for training our models, and for duplicating the data preprocessing that we performed. In this code we pull the data from https://www.basketball-reference.com/. This code should be run first, in order to generate the CSV file named NBA_Player_StatsV2. This code was written by Levi Kaster. 

    Alternatively the csv with the preprocessing already done can downloaded here [NBA_Player_StatsV2](https://wustl.box.com/s/mss2i89mx1f8me20ns7xqosdfarezzrn). 

2. [kNN Regression](https://github.com/kasterlevi/CSE543_NBA_Project/blob/main/k-nearest-neigbors.ipynb): This is the code that we used to run our kNN model. The code given links to the CSV file from this respository, so it can be run without the need to download the CSV from step 1. 
3. [Linear Regression](https://github.com/kasterlevi/CSE543_NBA_Project/blob/main/Linear%20Regression.ipynb): The code that we used to create the Linear Model used in our paper can be found here. The code given links to the CSV file from this respository, so it can be run without the need to download the CSV from step 1.
4. [Random Forest](https://github.com/kasterlevi/CSE543_NBA_Project/blob/main/randomforest.py): The code that we used to create the Random Forest Model used in our paper can be found here. The code contains a link to the CSV that we used already, but it can be downloaded from step 1 as well. Run the code to duplicate our results. This code was written by Patrick Norrick
5. [Deep Neural Network](https://github.com/kasterlevi/CSE543_NBA_Project/blob/main/NBA_DNN.ipynb): The code that we used to create the DNN used in our paper can be found here. The code contains a link to the CSV that we used already, but it can be downloaded from step 1 as well.

        This code was initially created in google colab, and this original code can be found [here](https://colab.research.google.com/drive/1aSjpmnt8ETarmQxnMOaok3HXYp71tTSm)
