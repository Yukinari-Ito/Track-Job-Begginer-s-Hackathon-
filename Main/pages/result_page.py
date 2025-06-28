import streamlit as st
from features.result import result, get_result, diagnosis

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>診断結果</h1>", unsafe_allow_html=True)

result_dict = st.session_state.result

result_val = result(result_dict)

diagnosis_result = get_result(result_val)

diagnosis = diagnosis(diagnosis_result)

st.markdown("<h3 style='text-align: center; color: #FF4B4B;'>診断結果</h3>", unsafe_allow_html=True)

st.