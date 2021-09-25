import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression

def select_kbest(X, y, k):
    '''
    Takes in predictors, target, and number of features to select and returns that number of best features based on SelectKBest function
    '''
    kbest = SelectKBest(f_regression, k=k)
    kbest.fit(X, y)
    return X.columns[kbest.get_support()].tolist()

def rfe(X, y, n):
    '''
    Takes in predictors, target, and number of features to select and returns that number of best features based on RFE function
    '''
    rfe = RFE(estimator=LinearRegression(), n_features_to_select=n)
    rfe.fit(X, y)
    return X.columns[rfe.get_support()].tolist()

def show_rfe_feature_ranking(X, y):
    '''
    Takes in predictors and target and returns feature ranking based on RFE function
    '''
    rfe = RFE(estimator=LinearRegression(), n_features_to_select=1)
    rfe.fit(X, y)
    rankings = pd.Series(rfe.ranking_, index=X.columns)
    return rankings.sort_values()