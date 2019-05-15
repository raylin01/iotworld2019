from flask import Flask, render_template, request
from keras.models import load_model
import tensorflow as tf
import numpy as np
import json
import requests
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)

model = load_model("lstm.h5")
graph = tf.get_default_graph()

def pred(vals):
	with graph.as_default():
		vals = np.array(vals)
		vals = vals.reshape((1, vals.shape[0], vals.shape[1]))
		prediction = model.predict(vals)
	return prediction

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/control')
def control():
	data = [
    [25, 0],
    [12, 0.2],
    [11, 0.2],
    [18, 0.6],
    [18, 0],
    [3, 0.1],
    [25, 0]
    ]
	# r = requests.post(url = "http://localhost:5000/api", data = data)
	curdata = pred(data)[0][0]
	watering = "should not " if (curdata < 0.5) else "should "
	content = "Prediction: " + str(curdata) + "<br/>You "+ watering + "water your plants"
	return render_template('control.html', content = content, data = data)

@app.route('/sensors')
def sensors():
	f=open("./sensors.json", "r")
	if f.mode == 'r':
		contents = json.loads(f.read())
		print(contents)
		sensors = ""
		for k,v in contents.items():
			try:
				if v == 'sensorip':
					raise Exception('You have not update your sensor IPS! Check sensors.json')
				url = "http://"+v+":5000/api"
				print(url)
				r = requests.get(url = url)
				value = r.text
			except:
				value = "Sensor Offline"
			sensors += str(k) + " Current Value: <br/>" + str(value) +"<br/>"
		return render_template('sensors.html', sensordata=sensors)
	else:
		return 'Sensor.json config not found'

@app.route('/api', methods=["GET", "POST"])
def api():
        if request.method == "POST":
        	output = pred(data)
        	return render_template('api.html', data = output)

if __name__ == '__main__':
	#load_lstm()
	app.run(debug=True, host='0.0.0.0')
