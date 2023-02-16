# -*- coding: utf-8 -*-
"""Iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IIhVzAjaUAGk4asyJV_3V9lLt3-9LXHc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

df=pd.read_csv("Iris.csv")
df

df.info

df.isnull().sum()

df.columns

df.describe

df=df.drop(columns="Id")

df

df['Species'].value_counts()

sns.countplot(df['Species'])

df.corr

df.describe()

df.tail()

df.nunique()

df.Species

plt.figure(figsize=(10,10))
sns.heatmap(data=df.corr(),annot=True,cmap='Blues')

#boxplot
plt.figure(figsize=(10,10))
df.boxplot()

sns.pairplot(df, size=3)

#x=independent variable,y=dependent varible
x=df.iloc[:,:4]
y=df.iloc[:,4]

x

y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=0)

x_train.shape

x_test.shape

y_train.shape

y_test.shape

model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

y_pred

confusion_matrix(y_test,y_pred)

accuracy=accuracy_score(y_test,y_pred)*100
print("Accuracy of model={:.2f}".format(accuracy))