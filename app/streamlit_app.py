import streamlit as st
import joblib
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import extract_features
        
        
# --- Set page configuration ---
st.set_page_config(page_title="Password Strength Detector", page_icon="🔐", layout="centered")

# --- Load the pre-trained model and vectorizer ---
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(base_dir, "models/password_model.pkl"))
vectorizer = joblib.load(os.path.join(base_dir, "models/vectorizer.pkl"))
scaler = joblib.load(os.path.join(base_dir, "models/scaler.pkl"))


# --- Interface design ---

st.markdown("""
<style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 2.2em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .footer {
        font-size: 0.8em;
        color: gray;
        text-align: center;
        margin-top: 2em;
    }
</style>
""", unsafe_allow_html=True)


st.title("🔐 Password Strength Detector")
st.write("Enter a password to check its strength based on a pre-trained model.")

default_pwd = st.session_state.get("generated_pwd", "")
password = st.text_input("Introduce your password", type="password", value=default_pwd, label_visibility="collapsed",
                         placeholder="Introduce your password here...")


# --- Prediction ---
if password:
    X, _ = extract_features([password], vectorizer, scaler, fit_scaler=False)
    prediction = model.predict(X)[0]  
      
    if prediction == 1:
        st.success("✅ Strong password!")
    else:
        st.error("❌ Weak password!")
            

# Footer 
st.markdown('<div class="footer">Educational project created by Jorge Illera Rivera • No passwords are stored</div>',
            unsafe_allow_html=True)
