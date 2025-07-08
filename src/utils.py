import math
import scipy.sparse
from sklearn.preprocessing import StandardScaler


def calc_entropy(pwd):
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in "!@#$%^&*()-_+=[]{};:'\",.<>/?\\|" for c in pwd): charset += 32
    if charset == 0: return 0
    return round(len(pwd) * math.log2(charset), 2)

def extract_features(passwords, vectorizer, scaler=None, fit_scaler=False):
    tfidf = vectorizer.transform(passwords)
    
    # Extra features
    lengths = [[len(p)] for p in passwords]
    entropies = [[calc_entropy(p)] for p in passwords]
    extra = [length + entropy for length, entropy in zip(lengths, entropies)]
    
    # Escalado
    if scaler is None:
        scaler = StandardScaler()
        fit_scaler = True
        
    if fit_scaler:
        extra_scaled = scaler.fit_transform(extra)
    else:
        extra_scaled = scaler.transform(extra)
        
    X_final = scipy.sparse.hstack([tfidf, extra_scaled])
    return X_final, scaler


