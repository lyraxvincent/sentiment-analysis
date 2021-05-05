from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import numpy as np
import pickle5 as pickle
import sklearn

app = Flask(__name__)

model = pickle.load(open('saved_model.pkl', 'rb'))
#cols = ['text', '', '']
cols = ['text']


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = int(model.predict(data_unseen.text))

    if prediction == -1:
        pred_display = "Negative \U0001F613"
    elif prediction == 0:
        pred_display = "Neutral \U0001F60C"
    else:
        pred_display = "Positive \U0001F60A"

    return render_template('home.html', pred='Sentiment: {}'.format(pred_display))

"""
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = model.predict(data_unseen)
    output = int(prediction)
    return jsonify(output)"""

if __name__ == '__main__':
    app.run()#debug=True)
