# 🎮 Game Classification – LLM Zero-Shot Project

## 👥 Integrantes
* *Claudio Dias Alves* – RA: 10403569
* *Daniel Rubio Camargo* – RA: 10408823
* *João Pedro Mascaro Baccelli* – RA: 10224004

---

# 📘 Introdução

Este projeto faz parte do *End-to-End AI Open Project* e segue a *Opção 1 – Text Classification (foco em LLMs)* apresentada pelo professor.

Nosso objetivo é classificar descrições de jogos em gêneros como Action, Adventure, RPG, Shooter, Strategy, Puzzle e Horror usando *modelos de linguagem (LLMs)* sem a necessidade de treinamento tradicional.

Utilizamos a técnica de *Zero-Shot Classification*, onde o modelo consegue prever um rótulo mesmo sem ter sido treinado especificamente nesse dataset. O usuário insere a descrição de um jogo na interface — e o LLM responde com o gênero mais provável.

---

# 🧠 Tecnologias Utilizadas

* *Python 3.11*
* *Transformers (Hugging Face)*
    * Modelo utilizado: valhalla/distilbart-mnli-12-1
* *Streamlit* (Front-End)
* *Requests / Pandas* (Coleta e manipulação opcional)
* *Jupyter Notebook* (Documentação e demonstração)

---

# 🛠️ Arquitetura do Projeto

### 🔹 1. Coleta e Análise de Dados (data_collection.ipynb)
Coleta de dados (opcional) via RAWG API, limpeza de descrições e organização do dataset.

### 🔹 2. Classificação com LLM (llm_classification.ipynb)
Notebook que demonstra e valida o funcionamento do modelo Zero-Shot.

### 🔹 3. Aplicação final (app_streamlit/app.py)

---

# Exemplos

<img width="818" height="518" alt="image" src="https://github.com/user-attachments/assets/ca97166e-8ee2-4a2f-a429-cf5804d50e66" />

<img width="818" height="518" alt="image" src="https://github.com/user-attachments/assets/61a43867-c0ea-43ff-a3d3-47315673b405" />

Interface onde o usuário digita a descrição do jogo e recebe o gênero previsto.

