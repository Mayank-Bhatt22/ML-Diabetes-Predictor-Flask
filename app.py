from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load trained pipeline
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # ==============================
        # GET INPUTS FROM FORM
        # ==============================
        pregnancies = float(request.form['Pregnancies'])
        age = float(request.form['Age'])
        glucose_cat = request.form['Glucose_Level']
        bp_cat = request.form['BP_Level']
        skin_cat = request.form['Skin_Level']
        bmi_cat = request.form['BMI_Category']
        dpf_cat = request.form['Genetic_Risk']
        age_group = request.form['Age_Group']

        # ==============================
        # CREATE DATAFRAME
        # ==============================
        input_data = pd.DataFrame([{
            'Pregnancies': pregnancies,
            'Age': age,
            'Glucose_Level': glucose_cat,
            'BP_Level': bp_cat,
            'Skin_Level': skin_cat,
            'BMI_Category': bmi_cat,
            'Genetic_Risk': dpf_cat,
            'Age_Group': age_group
        }])

        # ==============================
        # PREDICTION
        # ==============================
        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0]
        risk_percent = round(proba[1] * 100, 1)

        if prediction == 1:
            result = "Diabetic"
            result_class = "diabetic"
            result_icon = "⚠️"
            result_msg = "High risk detected. Please consult a medical professional immediately."
        else:
            result = "Healthy"
            result_class = "healthy"
            result_icon = "✅"
            result_msg = "No diabetes detected. Keep maintaining a healthy lifestyle!"

        # Build summary tags
        tags = [
            glucose_cat,
            f"BP: {bp_cat}",
            f"BMI: {bmi_cat}",
            f"Genetic Risk: {dpf_cat}",
            age_group
        ]

        return render_template(
            "index.html",
            prediction_text=f"{result_icon} {result}",
            result_class=result_class,
            result_msg=result_msg,
            risk_percent=risk_percent,
            tags=tags,
            show_result=True
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
            show_result=False
        )


if __name__ == "__main__":
    app.run(debug=True)
