import streamlit as st

st.title("Title")

post_content = st.text_area("Post Content", height=300)

st.button('投稿する')