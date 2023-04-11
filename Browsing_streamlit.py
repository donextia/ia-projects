import streamlit as st
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

openai_api_key = st.secrets["openai_api_key"]
serpapi_api_key = st.secrets["serpapi_api_key"]

os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["SERPAPI_API_KEY"] = serpapi_api_key

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def llamar_api_externa(texto):
    respuesta = agent.run(texto)
    return respuesta

st.title("AInnovation Demos")
st.tittle("ChatGPT connected to internet")

pregunta = st.text_input("¿Cómo te puedo ayudar?")
boton_obtener = st.button("Obtener respuesta")

if boton_obtener:
    respuesta = llamar_api_externa(pregunta)
    st.write("Esta es la respuesta:")
    st.write(respuesta)
