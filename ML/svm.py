from sklearn import svm
from sklearn import preprocessing
import numpy as np
import pandas as pd

dataframe = pd.read_csv('squaw_valley_delta.csv', sep=',', header=0)
dataframe = dataframe.dropna()
print(dataframe.isnull().any().any())
del dataframe['Date']
npdata = np.asarray(dataframe)
x = npdata[:,:4]
y = npdata[:, 4]
x = preprocessing.normalize(x, axis=0)

classifier = svm.SVR()
classifier.fit(x,y)

score = classifier.score(x,y)
print(score)
