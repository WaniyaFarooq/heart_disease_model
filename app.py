import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️")
st.title("Heart Disease Prediction")
st.warning("Educational demonstration only. This tool is not a medical diagnosis and must not guide treatment decisions.")

MODEL_PATH = Path(__file__).with_name("heart_disease_model.joblib")
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.write("Enter the four attributes used by the trained model.")
age = st.number_input("Age (years)", min_value=1, max_value=120, value=50)
sex_label = st.selectbox("Sex (dataset coding)", ["Female (0)", "Male (1)"])
sex = 0 if sex_label.startswith("Female") else 1
cp = st.selectbox("Chest-pain type (cp code)", [1, 2, 3, 4], index=1)
thalach = st.number_input("Maximum heart rate achieved (thalach)", min_value=50, max_value=250, value=150)

if st.button("Predict"):
    X = pd.DataFrame([{"age": age, "sex": sex, "cp": cp, "thalach": thalach}])
    pred = int(model.predict(X)[0])
    prob = float(model.predict_proba(X)[0, 1])
    if pred == 1:
        st.error(f"Model output: disease-present class (1). Estimated class-1 probability: {prob:.1%}")
    else:
        st.success(f"Model output: no-disease class (0). Estimated class-1 probability: {prob:.1%}")
    st.caption("This output is not a diagnosis. Consult a qualified healthcare professional for medical concerns.")
