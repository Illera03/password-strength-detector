from tqdm import tqdm
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from utils import extract_features
from sklearn.metrics import classification_report
import joblib


# --- Load passwords ---
def load_passwords():
    
    # Load weak passwords
    with open("data/rock_you_filtered.txt", "r", encoding = "utf-8") as f:
        weak_passwords = [(line.strip(), 0) for line in f if line.strip()]
        
    # Load strong passwords
    with open("data/strong_passwords.txt", "r", encoding = "utf-8") as f:
        strong_passwords = [(line.strip(), 1) for line in f if line.strip()]
    data = weak_passwords + strong_passwords
    df = pd.DataFrame(data, columns=["password","label"])
    return df

df = load_passwords()

# --- Vectorization ---
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 5), max_features=5000)
X_tfidf = vectorizer.fit_transform(df["password"])
X, scaler = extract_features(df["password"], vectorizer)
y = df["label"]


# --- Train model with progress bar ---
max_iter = 1000
model = LogisticRegression(class_weight="balanced", max_iter=1, warm_start=True, random_state=42, solver="lbfgs")
for i in tqdm(range(max_iter), desc="Entrenando modelo"):
    model.fit(X, y)


# --- Evaluate model ---
print(classification_report(y, model.predict(X)))


# --- Save model, vectorizer and scaler ---
joblib.dump(model, "models/password_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ Model, vectorizer and scaler saved on /models")
