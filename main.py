import streamlit as st

from src.application.domain import criptografa, descriptografa

st.title("Cifra de César")

st.session_state.frase = st.text_area(label='Mensagem')
st.session_state.chave = st.number_input('Chave',min_value=1, max_value=25, step=1)

col1, col2 = st.columns([.2,1])
with col1:
    st.button('Codificar', on_click=criptografa)
with col2:
    st.button('Decodificar', on_click=descriptografa)

if 'resultado' in st.session_state:
    st.write(f"Resultado: {st.session_state.resultado}")




