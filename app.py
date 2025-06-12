from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(_name_)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        data = np.array([features])
        result = model.predict(data)
        return render_template('index.html', prediction_text=f'Predicted Price: ${result[0]:.2f}K')
    except:
        return render_template('index.html', prediction_text="⚠ Invalid input.")

if _name_ == '_main_':
    app.run(debug=True)
