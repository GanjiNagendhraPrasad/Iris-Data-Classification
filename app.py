from flask import Flask, render_template, request
import numpy as np
import pickle
import json

# Load models
with open('Knn.pkl', 'rb') as f:
    knn_model = pickle.load(f)

with open('Nb.pkl', 'rb') as f:
    nb_model = pickle.load(f)

# Load performance JSON files
with open('knn_test_performance.json', 'r') as f:
    knn_performance = json.load(f)

with open('nb_test_performance.json', 'r') as f:
    nb_performance = json.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    performance = None
    selected_model = None

    if request.method == 'POST':
        sl = float(request.form['SepalLengthCm'])
        sw = float(request.form['SepalWidthCm'])
        pl = float(request.form['PetalLengthCm'])
        pw = float(request.form['PetalWidthCm'])
        selected_model = request.form['algorithm']

        features = np.array([[sl, sw, pl, pw]])

        if selected_model == "knn":
            pred = knn_model.predict(features)[0]
            performance = knn_performance
        else:
            pred = nb_model.predict(features)[0]
            performance = nb_performance

        if pred == 0:
            prediction = "Setosa"
        elif pred == 1:
            prediction = "Versicolor"
        else:
            prediction = "Virginica"

    return render_template(
        'index.html',
        prediction=prediction,
        performance=performance,
        selected_model=selected_model
    )

if __name__ == '__main__':
    app.run(debug=True)
