import streamlit as st
import pandas as pd

df = pd.DataFrame({ 'first' : [1,2,3,4,5] , 
                    'second' : [4,5,6,3,3], 'third': [4,2,2,4,6], 'fourth': [2,3,0,1,2]})

df

st.markdown("Thats it for today")

