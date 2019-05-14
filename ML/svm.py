from sklearn import svm
from sklearn import tree
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import *
from sklearn.tree import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

dataframe = pd.read_csv('atlanta_1980.csv')
dataframe = dataframe.dropna()
print(dataframe.isnull().any().any())
del dataframe['Date']
dataframe["Change In Soil Moisture Percent -8in (pct)"] = np.where(dataframe["Change In Soil Moisture Percent -8in (pct)"] >= 0, 0, dataframe["Change In Soil Moisture Percent -8in (pct)"])
dataframe["Change In Soil Moisture Percent -8in (pct)"] = np.where(dataframe["Change In Soil Moisture Percent -8in (pct)"] < 0, 1, dataframe["Change In Soil Moisture Percent -8in (pct)"])
npdata = np.asarray(dataframe)
np.random.shuffle(npdata)
print(npdata.shape)
x = npdata[:,:4]
y = npdata[:, 4].reshape(-1,1)
y = y.reshape((y.shape[0]))
print(x)
print(y)
train_split = int(0.9*x.shape[0])
x_train = x[:train_split,:]
y_train = y[:train_split]
x_test = x[train_split:x.shape[0],:]
y_test = y[train_split:x.shape[0]]

classifier = DecisionTreeClassifier(criterion='entropy', max_features=4)
classifier.fit(x_train,y_train)

score = classifier.score(x_train,y_train)
print(score)
tscore = classifier.score(x_test,y_test)
print(tscore)

