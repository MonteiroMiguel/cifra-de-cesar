import streamlit as st
from unidecode import unidecode 
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def criptografa_alfabeto():
    st.session_state.alfabeto_criptografado = alfabeto[st.session_state.chave:] + alfabeto[:st.session_state.chave]

def criptografa():
    criptografa_alfabeto()
    st.session_state.resultado = ''
    st.session_state.mensagem = unidecode(st.session_state.mensagem)
    for letra in st.session_state.mensagem:
        if letra.lower() not in alfabeto:
            st.session_state.resultado += letra
        else:
            i = alfabeto.index(letra.lower())
            st.session_state.resultado += st.session_state.alfabeto_criptografado[i].upper() if letra == letra.upper() else st.session_state.alfabeto_criptografado[i]

def descriptografa():
    criptografa_alfabeto()
    st.session_state.resultado = ''
    st.session_state.mensagem = unidecode(st.session_state.mensagem)
    for letra in st.session_state.mensagem:
        if letra.lower() not in alfabeto:
            st.session_state.resultado += letra
       
        else:
            i = st.session_state.alfabeto_criptografado.index(letra.lower())
            st.session_state.resultado += alfabeto[i].upper() if letra == letra.upper() else alfabeto[i]
