import streamlit as st

import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="お笑い感性診断", page_icon="🎤", layout="centered")

# 表紙タイトル
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎉 お笑い感性診断 🎉</h1>", unsafe_allow_html=True)

# 
lottie_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jbrw3hcz.json")
if lottie_animation:
    st_lottie(lottie_animation, speed=1, height=200, key="explosion")

# 説明文
st.markdown("""
<div style="text-align:center; font-size:18px; color:#333333; max-width:700px; margin:auto;">
<p>全〇〇問の質問に答えるだけで、あなたのお笑い感性が丸わかり！</p>
<p>普段あなたが面白いと感じることには、ある共通点が…？</p>
<p>共通のお笑い感性を持つ友達を作ろう！</p>
<p>あなたの好きな芸人さんにも出会えるかも…！？</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ボタンで診断スタート
start = st.button("🎬 診断スタート！", help="ここを押して診断を始めよう")





st.button('投稿する')