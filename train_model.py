import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# ---- 1. Carregar dataset ----
df = pd.read_csv("data/games.csv")   # precisa existir
X = df["description"]
y = df["genre"]

# ---- 2. Vetorização TF-IDF ----
vectorizer = TfidfVectorizer(stop_words="english")
X_tfidf = vectorizer.fit_transform(X)

# ---- 3. Treinar modelo ----
model = MultinomialNB()
model.fit(X_tfidf, y)

# ---- 4. Salvar modelo ----
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Modelo treinado e salvo!")