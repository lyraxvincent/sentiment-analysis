import streamlit as st
import pickle
import pandas as pd
import numpy as np

labels_dict = {-1: "Negative 😣", 0: "Neutral 😌", 1: "Positive 😊"}

text = st.text_input(label="Input text:", value="")

model = pickle.load(open('saved_model.pkl', 'rb'))
prediction = model.predict(pd.DataFrame([np.array(text)], columns=['text']).text)

with st.container():
    col1, col2, _,_,_ = st.columns(5)

    with col1:
        st.caption("Predicted sentiment: ")

    with col2:
        st.markdown(f":green[{pd.Series(prediction).map(labels_dict).values[0]}]")
