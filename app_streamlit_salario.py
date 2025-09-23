import streamlit as st
import json
import requests

# Titulo da aplicação
st.title("Modelo de Predição de Salário")

#Input do usuário
st.write("Quantos meses o profissional esta na empresa?")
tempo_na_empresa = st.slider("Meses", min_value=1, max_value=120, value=60, step=1)

st.write("Qual o nivel do profissional na empresa?")
nivel_na_empresa = st.slider("Nivel", min_value=1, max_value=10, value=5, step=1)

# Preparar os dados para a requisição
input_features = {
    "tempo_na_empresa": tempo_na_empresa,
    "nivel_na_empresa": nivel_na_empresa
}

# Criar um botao e capturar um evento deste botao para disparar a API
if st.button("Estimar Salário"):
    # Fazer a requisição para a API
    api_url = "http://127.0.0.1:8000/predict"  # Substitua pela URL correta da sua API
    res = requests.post(api_url, data=json.dumps(input_features))
    
    if res.status_code == 200:
        prediction = json.loads(res.text)
        salario_estimado = round(prediction['salario_em_reais'], 2)
        st.subheader(f"O salário estimado é: R$ {salario_estimado}")
    else:
        st.error("Erro ao conectar com a API.")