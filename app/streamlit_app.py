import streamlit as st
import joblib
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import extract_features


# --- Load the pre-trained model and vectorizer ---
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(base_dir, "models/password_model.pkl"))
vectorizer = joblib.load(os.path.join(base_dir, "models/vectorizer.pkl"))
scaler = joblib.load(os.path.join(base_dir, "models/scaler.pkl"))


# --- Interface design ---
st.title("🔐 Password Strength Detector")
st.write("Enter a password to check its strength based on a pre-trained model.")

password = st.text_input("Password", type="password")


# --- Prediction ---
if password:
    X, _ = extract_features([password], vectorizer, scaler, fit_scaler=False)
    prediction = model.predict(X)[0]    
    
    if prediction == 1:
        st.success("✅ This is a strong password!")
    else:
        st.error("❌ This is a weak password. Consider using a mix of letters, numbers, and special characters.")
    