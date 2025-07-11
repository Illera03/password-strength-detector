import os
import itertools
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
from utils import extract_features
import joblib
from tqdm import tqdm

# --- CONFIG ---
CHUNK_SIZE = 500_000
EPOCHS = 2

weak_path = "data/rock_you_filtered.txt"
strong_path = "data/strong_passwords.txt"

# --- Load password chunks ---
def load_chunk(filepath, label, start, size):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = itertools.islice(f, start, start + size)
        return [(line.strip(), label) for line in lines if line.strip()]

# --- Generator for training batches ---
def chunk_generator(chunk_size=CHUNK_SIZE):
    weak_len = sum(1 for _ in open(weak_path, "r", encoding="utf-8"))
    strong_len = sum(1 for _ in open(strong_path, "r", encoding="utf-8"))
    total_chunks = min(weak_len, strong_len) // chunk_size

    for i in range(total_chunks):
        weak_chunk = load_chunk(weak_path, 0, i * chunk_size, chunk_size)
        strong_chunk = load_chunk(strong_path, 1, i * chunk_size, chunk_size)
        data = weak_chunk + strong_chunk
        df = pd.DataFrame(data, columns=["password", "label"])
        yield df

# --- TF-IDF Initialization with progress ---
print("📦 Fitting TfidfVectorizer on first chunk...")
first_chunk = next(chunk_generator())
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 5), max_features=5000)

# Add fake progress bar (TF-IDF doesn't expose progress)
with tqdm(total=100, desc="Fitting TF-IDF", unit="%", ncols=80) as pbar:
    X_vec = vectorizer.fit_transform(first_chunk["password"])
    for i in range(100):
        pbar.update(1)

# --- Feature extraction ---
X_feat, scaler = extract_features(first_chunk["password"], vectorizer)
y = first_chunk["label"]

# --- Initialize incremental model ---
model = SGDClassifier(loss="log_loss", random_state=42)

print("🚀 Starting incremental training...")
for epoch in range(EPOCHS):
    print(f"🔁 Epoch {epoch + 1}/{EPOCHS}")
    gen = chunk_generator()
    for df in tqdm(gen, desc=f"Epoch {epoch + 1}", unit="chunk"):
        X_feat, _ = extract_features(df["password"], vectorizer, scaler)
        y = df["label"]
        model.partial_fit(X_feat, y, classes=[0, 1])

# --- Basic evaluation on last chunk ---
print("✅ Training complete.")
print("📊 Evaluation on last batch:")
print(classification_report(y, model.predict(X_feat)))

# --- Save model and vectorizer ---
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/password_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("💾 Model, vectorizer and scaler saved to /models")
