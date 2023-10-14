import streamlit as st
import pandas as pd

# Writing out the title and a paragraph
st.title("Gba AI")
st.write("Conventional gba LLM lol. Lets have some fun")

with st.markdown("Gbaman"):
  st.write("Welcome to gba land, nigga!")

user_message = st.text_input("You:", "")

if user_message:
  st.markdown(f"You: {user_message}")

response = "Hello!, This is Gba AI"

st.markdown(f"chatbot: {response}")
