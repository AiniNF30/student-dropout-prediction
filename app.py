import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


def predict_dropout(data, model_and_scaler):
    model = model_and_scaler['model']
    scaler = model_and_scaler['scaler']
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)
    return prediction

st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #4CAF50;
        font-size: 40px;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .input-container {
        margin-bottom: 20px;
    }
    .stTextInput>div {
        margin-top: 10px;
    }
    .stSelectbox>div {
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Student Dropout Prediction</h1>", unsafe_allow_html=True)

model_and_scaler = joblib.load('model/model.joblib')

def selectbox_yes_no(label):
    mapping = {"No": 0, "Yes": 1}
    selected = st.selectbox(label, list(mapping.keys()), key=label)
    return mapping[selected]

def selectbox_male_female(label):
    mapping = {"Female": 0, "Male": 1}
    selected = st.selectbox(label, list(mapping.keys()), key=label)
    return mapping[selected]

def selectbox_application_method(label):
    mapping = {
        "1st phase - general contingent": 1,
        "Ordinance No. 612/93": 2,
        "1st phase - special contingent (Azores Island)": 5,
        "Holders of other higher courses": 7,
        "Ordinance No. 854-B/99": 10,
        "International student (bachelor)": 15,
        "1st phase - special contingent (Madeira Island)": 16,
        "2nd phase - general contingent": 17,
        "3rd phase - general contingent": 18,
        "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
        "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
        "Over 23 years old": 39,
        "Transfer": 42,
        "Change of course": 43,
        "Technological specialization diploma holders": 44,
        "Change of institution/course": 51,
        "Short cycle diploma holders": 53,
        "Change of institution/course (International)": 57
    }
    selected = st.selectbox(label, list(mapping.keys()), key=label)
    return mapping[selected]

curricular_units_1st_sem_grade = st.number_input("Curricular Unit 1st Grade", min_value=0.0, max_value=26.0, value=5.0, key="Curricular_Unit_1st_Grade")
curricular_units_1st_sem_approve = st.number_input("Curricular Unit 1st Approved", min_value=0.0, max_value=20.0, value=10.0, key="Curricular_Unit_1st_Approved")
curricular_units_2nd_sem_grade = st.number_input("Curricular Unit 2nd Grade", min_value=0.0, max_value=20.0, value=10.0, key="Curricular_Unit_2nd_Grade")
curricular_units_2nd_sem_approve = st.number_input("Curricular Unit 2nd Approved", min_value=0.0, max_value=20.0, value=10.0, key="Curricular_Unit_2nd_Approved")

tuition_fees_up_to_date = selectbox_yes_no("Tuition fees up to date?")
scholarship_holder = selectbox_yes_no("Scholarship Holder?")
application_mode = selectbox_application_method("Application Mode")
gender = selectbox_male_female("Gender")
age_at_enrollment = st.number_input("Age at Enrollment", min_value=17, max_value=100, value=20, key="Age_at_Enrollment")
debtor = selectbox_yes_no("Debtor?")

features = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Tuition_fees_up_to_date',
    'Scholarship_holder',
    'Application_mode',
    'Gender',
    'Age_at_enrollment',
    'Debtor'
]

user_data = pd.DataFrame([[curricular_units_1st_sem_grade,
                           curricular_units_1st_sem_approve,
                           curricular_units_2nd_sem_grade,
                           curricular_units_2nd_sem_approve,
                           tuition_fees_up_to_date,
                           scholarship_holder,
                           application_mode,
                           gender,
                           age_at_enrollment,
                           debtor]],
                         columns=features)

if st.button("Predict Dropout"):
    result = predict_dropout(user_data, model_and_scaler)
    if result[0] == 1:
        st.error("⚠️ The student is likely to drop out.", icon="🚨")
    else:
        st.success("✅ The student is likely to stay enrolled.", icon="🎉")
