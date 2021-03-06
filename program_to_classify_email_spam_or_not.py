# -*- coding: utf-8 -*-
"""Program to classify email spam or not.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18-x8I9sJ5b-IfSnneCaWM5bkoDC4sS4B

# spam or not using logistic regression

## importing librariies
"""

import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""## load data"""

df= pd.read_csv('emails.csv')
df.head(10)

df.shape

df.isnull().sum()

df.describe()

df.corr()

X = df.iloc[:,1:3001]
X

y = df.iloc[:,-1].values
y

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25)

"""## Applay ML model"""

lr=LogisticRegression()
lr.fit(X_train,y_train)

y_pred=lr.predict(X_test)
print("Accuracy Score for Logistic Regression : ", accuracy_score(y_pred,y_test))