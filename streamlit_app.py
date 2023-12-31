import pandas as pd
import streamlit as st

st.title("Welcome to streamlit")
st.write("Hello, World!")
st.subheader("Hey, man")
st.markdown("Nice to have you here")

st.subheader("Watch this Karma video by Seyi Vibez")
st.video("https://youtu.be/dN4QxTcis2w?si=bX-CpK3fh3SjSzmQ")
st.caption("Karma - Seyi Vibez")


st.checkbox("yes", "No")
st.button("Click Now!")
st.radio('Pick your gender:', ["Male", "Female"])
st.selectbox('Pick your gender', ['male', 'female'])
st.multiselect("What country are you from?", ['Nigeria', 'Ghana', 'Togo', 'SA', 'USA'])

st.select_slider('Pick one of slide', ["Red", "Blue", "Purple", "Orange"])
st.slider('Pick a number', 0,100)
