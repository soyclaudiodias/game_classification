import streamlit as st
from transformers import pipeline  # LLM

# Carrega o modelo LLM
classifier_llm = pipeline(
    "zero-shot-classification",
    model="valhalla/distilbart-mnli-12-1"  # modelo mais leve e rápido
)

candidate_labels = ["Action", "Adventure", "RPG", "Shooter", "Strategy", "Puzzle", "Horror"]

st.set_page_config(page_title="Game Classifier", page_icon="🎮")

st.title("🎮 Game Classifier")
st.write("Digite a descrição de um jogo e o modelo tentará prever o gênero.")

texto = st.text_area("Descrição do jogo:", height=200)

if st.button("Classificar"):
    if not texto.strip():
        st.warning("Por favor, digite uma descrição primeiro.")
    else:
        result = classifier_llm(texto, candidate_labels)
        best_label = result["labels"][0]
        st.success(f"Gênero previsto (LLM): **{best_label}**")