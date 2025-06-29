import streamlit as st
from streamlit_lottie import st_lottie
from features.random_selection import shuffled_selection_values
from features.result import result, diagnosis_based_on_result, diagnosis_type, diagnosis_sentences
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def rerun():
    st.rerun()

st.set_page_config(page_title="お笑い感性診断", page_icon="🎤", layout="centered")

if 'page' not in st.session_state:
    st.session_state.page = 'top'

def show_top():
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎉 お笑い感性診断 🎉</h1>", unsafe_allow_html=True)
    lottie_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jbrw3hcz.json")
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=200, key="explosion")

    st.markdown("""
    <div style="text-align:center; font-size:18px; color:#333333; max-width:700px; margin:auto;">
    <p>全15問の質問に答えるだけで、あなたのお笑い感性が丸わかり！</p>
    <p>普段あなたが面白いと感じることには、ある共通点が…？</p>
    <p>共通のお笑い感性を持つ友達を作ろう！</p>
    <p>あなたの好きな芸人さんにも出会えるかも…！？</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("🎬 診断スタート！"):
        st.session_state.page = 'question_select'
        rerun()

def show_question_select():
    if 'questions' not in st.session_state:
        st.session_state.questions = shuffled_selection_values()
        st.session_state.question_keys = list(st.session_state.questions.keys())
        st.session_state.current_q_idx = 0
        st.session_state.answers = {}

    total_questions = 15
    current = st.session_state.current_q_idx

    if current < total_questions:
        key = st.session_state.question_keys[current]
        data = st.session_state.questions[key]

        st.markdown(f"## 質問 {current + 1} / {total_questions}")
        st.markdown(f"""
        <div style="text-align:center; font-size:22px; font-weight:bold; margin:30px 0;">
        {data['question']}
        </div>
        """, unsafe_allow_html=True)

        left_label = data['options'][0]
        right_label = data['options'][1]

        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            st.markdown(f"<p style='text-align:center; font-size:18px; color:#FF4B4B;'>{left_label}</p>", unsafe_allow_html=True)

        with col2:
            cols = st.columns(4)
            scores = [-1, -0.7, 0.7, 1]
            for i, col in enumerate(cols):
                with col:
                    if st.button("●", key=f"choice_{current}_{i}"):
                        st.session_state.answers[key] = scores[i]
                        st.session_state.current_q_idx += 1
                        rerun()

        with col3:
            st.markdown(f"<p style='text-align:center; font-size:18px; color:#4BA3FF;'>{right_label}</p>", unsafe_allow_html=True)
    else:
        st.markdown("全て回答しました")
        if st.button("結果を診断する"):
            st.session_state.page = 'result'
            rerun()


def show_result():
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>診断結果</h1>", unsafe_allow_html=True)

    result_dict = st.session_state.answers
    result_val = result(result_dict)
    diagnosis_result = diagnosis_based_on_result(result_val)
    diagnosis_val = diagnosis_type(diagnosis_result)
    diagnosis_sentence = diagnosis_sentences(diagnosis_val)

    st.markdown(f"<p style='text-align: center; font-size:18px; color: #ffffff;'>あなたのタイプは...</p>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: #ffffff;'>{diagnosis_val}</h3>", unsafe_allow_html=True)
    st.markdown(diagnosis_sentence, unsafe_allow_html=True)


# ページ遷移管理
if st.session_state.page == 'top':
    show_top()
elif st.session_state.page == 'question_select':
    show_question_select()
elif st.session_state.page == 'result':
    show_result()
