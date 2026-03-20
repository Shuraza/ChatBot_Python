import streamlit as st
from chat import Chat

st.set_page_config(page_title="ChatPyAI", layout="centered")

st.title("MucaChat")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chat()

if "historico" not in st.session_state:
    st.session_state.historico = []

pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar") and pergunta:
    resposta = st.session_state.chatbot.resposta_bot(pergunta)

    st.session_state.historico.append(("Você", pergunta))
    st.session_state.historico.append(("Bot", resposta))

for autor, msg in st.session_state.historico:
    if autor == "Você":
        st.markdown(f"**🧑 {autor}:** {msg}")
    else:
        st.markdown(f"**🤖 {autor}:** {msg}")