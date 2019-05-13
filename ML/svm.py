from sklearn import svm
from sklearn import preprocessing
from sklearn.linear_model import *
import numpy as np
import pandas as pd

dataframe = pd.read_csv('squaw_valley_2000.csv', sep=',', header=0)
dataframe = dataframe.dropna()
print(dataframe.isnull().any().any())
del dataframe['Date']
npdata = np.asarray(dataframe)
npdata = preprocessing.normalize(npdata, axis=1)
x = npdata[:,:4]
y = npdata[:, 4]
#x = preprocessing.normalize(x, axis=0)
#y = preprocessing.normalize(y.reshape(-1, 1), axis=0)
print(x)
print(y)
x_train = x[:2910,:]
y_train = y[:2910]
x_test = x[2910:3234,:]
y_test = y[2910:3234]

classifier = BayesianRidge()
classifier.fit(x_train,y_train)

score = classifier.score(x_train,y_train)
print(score)
tscore = classifier.score(x_test,y_test)
print(tscore)

