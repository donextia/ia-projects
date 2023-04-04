import streamlit as st
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# Reemplaza estas claves con las tuyas
openai_api_key = "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"
serpapi_key = "4c2bfea367cf7f7baac31858ad4693acb4446790aae847b924991029880b224e"

os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["SERPAPI_API_KEY"] = serpapi_key

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def llamar_api_externa(texto):
    respuesta = agent.run(texto)
   # resultado = agent.run(texto)
    #respuesta = resultado["choices"][0]["text"]
    return respuesta

st.title("donext IA projects- ChatGPT conectado a internet")

pregunta = st.text_input("¿Cómo te puedo ayudar?")
boton_obtener = st.button("Obtener respuesta")

if boton_obtener:
    respuesta = llamar_api_externa(pregunta)
    st.write("Esta es la respuesta:")
    st.write(respuesta)
