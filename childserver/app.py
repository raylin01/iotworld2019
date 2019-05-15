from flask import Flask, render_template, request
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
	f=open("./data.txt", "r")
	if f.mode == 'r':
		contents=f.read()
		return render_template('api.html', vals=contents)

@app.route('/changevals')
def changevals():
	return render_template('change.html')

@app.route('/update', methods=["GET", "POST"])
def update():
	if request.method == "POST":
		f = open("./data.txt", "w+")
		data = request.form
		f.write(json.dumps(data))
	return render_template('update.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
