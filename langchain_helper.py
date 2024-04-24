import streamlit as st 
from langchain.llms import Ollama
llm = Ollama(model="llama2-uncensored:latest") # 👈 stef default

st.title("Give me a prompt and I'll generate a response")

colA, colB = st.columns([.90, .10])
with colA:
    prompt = st.text_input("prompt", value="", key="prompt")
response = ""
with colB:
    st.markdown("")
    st.markdown("")
    if st.button("Go", key="button"):
        response = llm.predict(prompt)
st.markdown(response)