import streamlit as st
from transformers import pipeline

# Carrega o modelo LLM
classifier_llm = pipeline(
    "zero-shot-classification",
    model="valhalla/distilbart-mnli-12-1"
)

candidate_labels = ["Action", "Adventure", "RPG", "Shooter", "Strategy", "Puzzle", "Horror"]

st.set_page_config(page_title="Game Classifier", page_icon="🎮")

st.title("🎮 Game Classifier")
st.write("Digite a descrição de um jogo e o modelo tentará prever o gênero.")

texto = st.text_area("📘 Descrição do jogo:", height=200)

if st.button("Classificar"):
    if not texto.strip():
        st.warning("⚠️ Por favor, digite uma descrição primeiro.")
    else:
        with st.spinner("Analisando com o modelo LLM... 🤖"):
            result = classifier_llm(texto, candidate_labels)

        best_label = result["labels"][0]
        scores = result["scores"]

        # Resultado principal
        st.success(f"🎯 Gênero previsto: **{best_label}**")

        # Explicação adicional
        st.subheader("📊 Confiança do modelo")
        for label, score in zip(result["labels"], scores):
            st.write(f"• **{label}** → {score*100:.2f}%")

        # Barra de probabilidade
        st.progress(float(scores[0]))

        st.info("""
        **🧠 Como funciona?**  
        O modelo compara sua descrição com cada gênero e analisa qual é mais provável
        usando inferência lógica via NLI (Natural Language Inference).
        """)
