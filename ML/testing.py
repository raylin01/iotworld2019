from sklearn.externals import joblib
import numpy as np

model = joblib.load("decision_tree.pkl")

def pred(vals):
    vals = np.asarray(vals)
    vals = vals.reshape([1,-1])
    return model.predict(vals)

while True:
    humidity = float(input("Enter humidity %"))
    temp = float(input("Enter temp in F"))
    precip = float(input("Enter precipitation in inches"))
    precipdel = float(input("Change in precipitation in inches"))
    arr = [humidity, temp, precip, precipdel]
    print(str(pred(arr)))
