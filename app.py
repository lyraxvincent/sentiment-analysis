import streamlit as st
import pickle
import pandas as pd
import numpy as np

# page settings
st.set_page_config(layout="centered", page_icon="💬", page_title="sentlysis")
st.write(
    """
    <style>
    [data-testid="stMetricDelta"] svg {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True)
# hide "made with streamlit"
st.write("""
         <style>
         footer {visibility: hidden;}
         </style>
         """, unsafe_allow_html=True)
# hide header elements
st.markdown("""
            <style>
            #MainMenu, header {visibility: hidden;}
            </style>
            """, unsafe_allow_html=True)
# reduce whitespace pagetop
st.markdown(
    """
    <style>
    div.block-container {padding-top:1rem;}
    </style>
    """, unsafe_allow_html=True
)

# app logic
labels_dict = {-1: "Negative 😣", 0: "Neutral 😌", 1: "Positive 😊"}

text = st.text_input(label="Input text:", value="")

model = pickle.load(open('saved_model.pkl', 'rb'))
prediction = model.predict(pd.DataFrame([np.array(text)], columns=['text']).text)

with st.container():
    col1, col2, _,_,_ = st.columns(5)

    with col1:
        st.caption("Predicted sentiment: ")

    with col2:
        if text.strip() != "":
            st.markdown(f":green[{pd.Series(prediction).map(labels_dict).values[0]}]")
