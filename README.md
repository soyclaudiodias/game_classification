# 🎮 Game Classification – LLM Zero-Shot Project

## 👥 Integrantes
* **Claudio Dias Alves** – RA: 10403569  
* **Daniel Rubio Camargo** – RA: 10408823  
* **João Pedro Mascaro Baccelli** – RA: 10224004  

---

# 📘 Introdução

Este projeto foi desenvolvido como parte do **End-to-End AI Open Project**, seguindo a *Opção 1 – Text Classification (foco em LLMs)*.

O objetivo é **classificar descrições de jogos em gêneros** como:

> *Action, Adventure, RPG, Shooter, Strategy, Puzzle e Horror.*

Utilizamos o método **Zero-Shot Classification**, onde o modelo consegue prever um gênero mesmo sem ter sido treinado especificamente no nosso dataset.

O usuário insere uma descrição → o modelo analisa a semântica → retorna o gênero mais provável + probabilidades.

---

# 🧠 Tecnologias Utilizadas

- **Python 3.11**
- **Transformers (Hugging Face)**
  - Modelo: `valhalla/distilbart-mnli-12-1`
- **Streamlit** (Front-End)
- **Pandas / Requests** (Coleta e Organização)
- **Jupyter Notebook** (Documentação)

---

# 🏗️ Arquitetura do Projeto

```
📦 projeto-game-classification/
│
├── app_streamlit/
│   ├── app.py               # Aplicação final
│   └── requirements.txt     # Dependências
│
├── notebooks/
│   ├── data_collection.ipynb
│   ├── llm_classification.ipynb
│   └── model_training.ipynb
│
└── README.md
```

---

# 🔹 1. Coleta e Preparação de Dados  
📍 *Arquivo: `notebooks/data_collection.ipynb`*

Coleta opcional via RAWG API, limpeza textual e organização de descrições.

---

# 🔹 2. Classificação com LLM  
📍 *Arquivo: `notebooks/llm_classification.ipynb`*

Demonstração do modelo Zero-Shot, validação e explicação dos resultados.

---

# 🔹 3. Aplicação Final  
📍 *Arquivo: `app_streamlit/app.py`*

Interface Streamlit contendo:

- Campo de texto  
- Classificação em tempo real  
- Probabilidades  
- Feedback visual  
- Explicação do modelo  

---

# 🎨 Interface

<img width="818" height="518" src="https://github.com/user-attachments/assets/ca97166e-8ee2-4a2f-a429-cf5804d50e66" />

<img width="818" height="518" src="https://github.com/user-attachments/assets/61a43867-c0ea-43ff-a3d3-47315673b405" />

---

# 🚀 Como Executar o Projeto (SEM DOCKER)

```bash
git clone https://github.com/soyclaudiodias/game_classification.git
cd game_classification
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app_streamlit/app.py
```

Após rodar o comando acima, acesse:

```
http://localhost:8501
```

---

# 📊 Resultados

O modelo Zero-Shot é capaz de interpretar descrições e associá‑las ao gênero correto com boa precisão, sem treinamento prévio.

---

# 🎉 Conclusão

O projeto demonstra como **LLMs podem ser aplicados diretamente** para classificação de texto, reduzindo a necessidade de treinar modelos tradicionais. A interface Streamlit proporciona uma experiência clara e explicável.

---

