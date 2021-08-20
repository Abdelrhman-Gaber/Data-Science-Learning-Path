# -*- coding: utf-8 -*-
"""Second ML program - Random Forest sample.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_yLzX9BOkhDLX6sF9Lw6S4ye_jjkgvNb

# Second ML program - Random Forest sample
"""

import numpy as np
import pandas as pd

"""## read data"""

home_data = pd.read_csv('train.csv')
home_data.head()

"""## feature selection



"""

home_data.columns

y = home_data['SalePrice']

feature_names = ['LotArea','LotArea','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']

X = home_data[feature_names]

from sklearn.model_selection import  train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)

y_train = y_train.values.reshape(-1, 1)

"""## feature scaling"""

'''
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''

"""## applay random forest"""

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor()
regressor.fit(X_train,y_train)

from sklearn.metrics import mean_absolute_error
prediction = regressor.predict(X_test)

mae = mean_absolute_error(prediction,y_test)
mae

"""# conclusion

we can improve the result by choose another parameters
"""