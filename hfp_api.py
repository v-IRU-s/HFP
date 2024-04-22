from flask import Flask,request,jsonify
import pickle


model = pickle.load(open('HFP.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def predict():
    age = request.form.get("age")
    anaemia = request.form.get("anaemia")
    creatinine_phosphokinase = request.form.get("creatinine_phosphokinase")
    diabetes = request.form.get("diabetes")
    ejection_fraction = request.form.get("ejection_fraction")
    high_blood_pressure = request.form.get("high_blood_pressure")
    platelets = request.form.get("platelets")
    serum_creatinine = request.form.get("serum_creatinine")
    serum_sodium = request.form.get("serum_sodium")
    sex = request.form.get("sex")
    smoking = request.form.get("smoking")
    time = request.form.get("time")
    cholesterol = request.form.get("cholesterol")
    body_mass_index = request.form.get("body_mass_index")
    heart_rate = request.form.get("heart_rate")
    exercise_angina = request.form.get("exercise_angina")
    st_slope = request.form.get("st_slope")
    num_vessels = request.form.get("num_vessels")
    thalassemia = request.form.get("thalassemia")

    pred = model.predict([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure,
                           platelets, serum_creatinine, serum_sodium, sex, smoking, time, cholesterol, body_mass_index,
                           heart_rate, exercise_angina, st_slope, num_vessels, thalassemia]])



    return jsonify({'DEATH_EVENT':str(pred[0])})



