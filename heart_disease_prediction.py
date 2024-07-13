import numpy as np
import streamlit as st
import pickle

loaded_model = pickle.load(open('rg_trained_model.pkl', 'rb'))


def heart_disease_prediction(input_data):

    input = np.array(input_data).reshape(1, -1)

    prediction = loaded_model.predict(input)

    print(prediction)

    if prediction[0] == 0:
        return "No heart disease"
    else:
        return "Have Heart disease"
    
gender_string_labels = {0: "Female", 1: "Male"}

chest_pain_cat = {0: 'Typical Angina', 1: 'Atypical Angina', 2: 'Non-anginal pain', 3: 'Asymptomatic'}

fbs_cat = {0:"<= 120 mg/dL", 1:">120 mg/dL"}

restecg_cat = {0:"Normal", 1:"ST-T wave abnormality", 2:"Left ventricular hypertrophy (LVH)"}

exang_cat = {0:'No Exercise induced angina', 1:"Exercise induced angina"}

slope_cat = {0:'Up', 1:'Flat', 2:'Down'}

thal_cat = {0: "Normal blood flow", 1: "Fixed defect", 2: "Reversible defect"}

ca_cat = {0: "No coronary arteries affected", 1: "One coronary artery affected", 
          2: "Two coronary arteries affected", 3: "Three coronary arteries affected",
          4: "CABG (coronary artery bypass graft) present"}

    


def main():

    # Giving Title
    st.title("Heart Disease Prediction App")

    # Getting input data from user
    age = st.text_input('**Enter age**')

    gender = st.radio("**Select Gender**", options=list(gender_string_labels.keys()),
                       format_func=lambda x: gender_string_labels[x], horizontal=True)

    cp = st.selectbox("**Select Chest pain (cp)**", options=list(chest_pain_cat.keys()),
                      format_func=lambda x: chest_pain_cat[x])
    
    trestbps = st.text_input("**Enter Resting Blood pressure (trestbps)**")

    chol = st.text_input("**Enter Serum cholesterol (chol)**")

    fbs = st.radio("**Select Fasting Blood Sugar (fbs)**", options=list(fbs_cat.keys()),
                   format_func=lambda x: fbs_cat[x], horizontal=True)

    restecg = st.radio("**Select Resting ECG result (restecg)**", options=list(restecg_cat.keys()),
                       format_func=lambda x: restecg_cat[x])

    thalach = st.text_input("**Enter Maximum Heart Rate (thalach)**")

    exang = st.radio("**Select Exercise Induced Angina (exang)**", options=list(exang_cat.keys()),
                     format_func= lambda x: exang_cat[x])

    oldpeak = st.text_input("**Enter ST depression (mm)  (oldpeak)**")

    slope = st.radio("**Select Slope**", options=list(slope_cat.keys()),
                     format_func=lambda x: slope_cat[x], horizontal=True)

    ca = st.selectbox("**Select Number of Coronary Artery affected (ca)**", options=list(ca_cat.keys()),
                      format_func=lambda x: ca_cat[x])
    
    thal = st.selectbox("**Select Thallium stress (ca)**", options=list(thal_cat.keys()),
                        format_func=lambda x: thal_cat[x])
    
    prediction = ''

    if st.button('**Heat Disease Prediction**'):
        prediction = heart_disease_prediction([age, gender, cp, trestbps, chol, fbs, restecg, thalach,
                                               exang, oldpeak, slope, ca, thal])
        
        if prediction[0] == 0:
            return st.success(prediction)
        else:
            return st.warning(prediction)
        
        
# if __name__ == "__main__":
#     main()