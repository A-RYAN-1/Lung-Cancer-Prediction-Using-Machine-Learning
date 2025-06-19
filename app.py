from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load('./models/lung_cancer_model.pkl')
scaler = joblib.load('./models/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs in the same order as model expects
        data = [float(request.form.get(field)) for field in [
            'Age', 'Gender', 'Air Pollution', 'Alcohol use', 'Dust Allergy',
            'OccuPational Hazards', 'Genetic Risk', 'chronic Lung Disease',
            'Balanced Diet', 'Obesity', 'Smoking', 'Passive Smoker',
            'Chest Pain', 'Coughing of Blood', 'Fatigue', 'Weight Loss',
            'Shortness of Breath', 'Wheezing', 'Swallowing Difficulty',
            'Clubbing of Finger Nails', 'Frequent Cold', 'Dry Cough', 'Snoring'
        ]]

        # Scale and predict
        scaled = scaler.transform([data])
        prediction = model.predict(scaled)[0]

        # Map prediction to label
        label_map = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
        result = label_map.get(prediction, "Unknown")

        return render_template('index.html', prediction_text=f"Predicted Lung Cancer Risk: {result}")
    except Exception as e:
        return f"⚠️ Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)