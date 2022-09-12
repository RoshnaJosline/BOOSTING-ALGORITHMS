# -*- coding: utf-8 -*-
"""M5class(Advanced boosting cross validation Algorithm)-XGboost.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vsq_nmjAYMF59TEyf-T5SG4Ud1GZVu-h
"""

import pandas as pd
import numpy as np

df=pd.read_csv('/content/heart.csv')

df

df.shape

df.isnull().sum()

X=df.drop('output',axis=1)
y=df.output

pip install xgboost

from xgboost import XGBClassifier

from sklearn.model_selection import train_test_split,RepeatedStratifiedKFold,cross_val_score

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=0)

X.shape

y.shape

cv=RepeatedStratifiedKFold(n_splits=7,n_repeats=3,random_state=1)

model=XGBClassifier()

scores=cross_val_score(model,X,y,scoring='accuracy',cv=cv)

print('Accuracy is: ',np.mean(scores))