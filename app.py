import numpy as np
import pandas as pd
from flask import Flask,render_template, request
import pickle


app=Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaled.pkl","rb") as f:
    scale=pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=["POST"])
def predict():

    try:
        age = float(request.form["age"])
        sex = float(request.form["sex"])
        cp = float(request.form["cp"])
        thalach = float(request.form["thalach"])
        oldpeak = float(request.form["oldpeak"])
        slope = float(request.form["slope"])
        thal = float(request.form["thal"])

        input_data = np.array([[
            age,
            sex,
            cp,
            thalach,
            oldpeak,
            slope,
            thal
        ]])

        scaled_data = scale.transform(input_data)

        prediction = model.predict(scaled_data)[0]

        if prediction == 1:
            result = "Heart Disease Detected"
            result_type = "danger"
        else:
            result = "No Heart Disease Detected"
            result_type = "success"

        return render_template(
            "index.html",
            prediction=result,
            result_type=result_type
        )
    except Exception as e:
        # If an error occurs during POST, render the template with the error message
        prediction = f"Error: {str(e)}"
        return render_template("index.html", prediction=prediction)  # <--- Added return here for error handling



if __name__ == "__main__":
    app.run(debug=True)
