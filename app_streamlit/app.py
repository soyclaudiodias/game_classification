import streamlit as st
import joblib

# Carrega modelo e vetorizador
clf = joblib.load("model/classifier.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.set_page_config(page_title="Game Classifier", page_icon="🎮")

st.title("🎮 Game Classifier")
st.write("Digite a descrição de um jogo e o modelo tentará prever o gênero.")

texto = st.text_area("Descrição do jogo:", height=200)

if st.button("Classificar"):
    if not texto.strip():
        st.warning("Por favor, digite uma descrição primeiro.")
    else:
        vec = vectorizer.transform([texto])
        pred = clf.predict(vec)[0]
        st.success(f"Gênero previsto: **{pred}**")