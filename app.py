from flask import Flask,render_template,url_for,request
from joblib import load

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	pipeline = load('pipeline.joblib')

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		my_prediction = pipeline.predict(data)
	return render_template('home.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)