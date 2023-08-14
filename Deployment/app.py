import streamlit as st
import eda_fp
import prediction_fp

navigation = st.sidebar.selectbox('Pilih halaman :', ('EDA', 'Make a Prediction'))

if navigation == 'EDA' :
    eda_fp.run()
else :
    prediction_fp.run()