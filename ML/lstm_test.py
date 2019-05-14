from keras.models import load_model
import numpy as np

model = load_model('lstm.h5')

def pred(vals):
    vals = np.array(vals)
    vals = vals.reshape((1, vals.shape[0], vals.shape[1]))
    return model.predict(vals)

data = [
    [25, 0],
    [12, 0.2],
    [11, 0.2],
    [18, 0.6],
    [18, 0],
    [3, 0.1],
    [25, 0]
    ]

result = pred(data)
print(result)
