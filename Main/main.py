import streamlit as st
from streamlit_lottie import st_lottie
from features.random_selection import shuffled_selection_values
from features.result import result, diagnosis_based_on_result, diagnosis_type, diagnosis_sentences
import requests
import random
import time

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
    <div style="text-align:center; font-size:18px; max-width:700px; margin:auto;">
    <p>全15問の質問に答えるだけで、あなたのお笑い感性が丸わかり！</p>
    <p>普段あなたが面白いと感じることには、ある共通点が…？</p>
    <p>共通のお笑い感性を持つ友達を作ろう！</p>
    <p>あなたの好きな芸人さんにも出会えるかも…！？</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("🎬 診断スタート！"):
        st.session_state.page = 'example'
        rerun()


def show_example():
    st.markdown("## 例題 (ウォーミングアップ)")
    st.markdown("""
    <div style="text-align:center; font-size:22px; font-weight:bold; margin:30px 0;">
    好きなのは？
    </div>
    """, unsafe_allow_html=True)

    left_label = "夏"
    right_label = "冬"

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.markdown(f"<p style='text-align:center; font-size:18px; color:#FF4B4B;'>{left_label}</p>", unsafe_allow_html=True)

    with col2:
        cols = st.columns(4)
        for i, col in enumerate(cols):
            with col:
                if st.button("●", key=f"example_choice_{i}"):
                    st.session_state.page = 'question_select'
                    # 診断初期化
                    st.session_state.questions = shuffled_selection_values()
                    st.session_state.question_keys = list(st.session_state.questions.keys())
                    st.session_state.current_q_idx = 0
                    st.session_state.answers = {}
                    rerun()

    with col3:
        st.markdown(f"<p style='text-align:center; font-size:18px; color:#4BA3FF;'>{right_label}</p>", unsafe_allow_html=True)



def show_question_select():
    if 'questions' not in st.session_state:
        st.session_state.questions = shuffled_selection_values()
        st.session_state.question_keys = list(st.session_state.questions.keys())
        st.session_state.current_q_idx = 0
        st.session_state.answers = {}

    total_questions = 15
    current = st.session_state.current_q_idx

    display_idx = min(current + 1, total_questions)
    st.markdown(f"## 質問 {display_idx} / {total_questions}")

    progress_ratio = display_idx / total_questions
    progress_html = f"""
    <div style='width:100%; background:#e0e0e0; height:20px; border-radius:10px;'>
        <div style='width:{progress_ratio*100}%; background:#FF4B4B; height:20px; border-radius:10px;'></div>
    </div>
    """
    st.markdown(progress_html, unsafe_allow_html=True)

    if current < total_questions:
        key = st.session_state.question_keys[current]
        data = st.session_state.questions[key]

        st.markdown(f"""
        <div style="text-align:center; font-size:22px; font-weight:bold; margin:30px 0;">
        {data['question']}
        </div>
        """, unsafe_allow_html=True)

        if random.choice([True, False]):
            left_label = data['options'][1]
            right_label = data['options'][0]
            scores = [1, 0.7, -0.7, -1]
        else:
            left_label = data['options'][0]
            right_label = data['options'][1]
            scores = [-1, -0.7, 0.7, 1]

        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            st.markdown(f"<p style='text-align:center; font-size:18px; color:#FF4B4B;'>{left_label}</p>", unsafe_allow_html=True)

        with col2:
            cols = st.columns(4)
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
            st.session_state.page = 'loading'
            rerun()

def show_loading():
        st.empty()
        spinner_html = """
        <div style="display: flex; justify-content: center; align-items: center; height: 80vh;">
        <div style="text-align: center;">
            <div style="
            border: 16px solid #f3f3f3;
            border-top: 16px solid #3498db;
            border-radius: 50%;
            width: 120px;
            height: 120px;
            animation: spin 2s linear infinite;
            margin: auto;
            "></div>
            <p style="margin-top: 20px; font-size: 24px;">診断中...</p>
        </div>
        </div>

        <style>
        @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
        }
        </style>
        """

        # スピナーを表示
        placeholder = st.empty()
        placeholder.markdown(spinner_html, unsafe_allow_html=True)

        # 擬似的な処理時間
        time.sleep(3)

        # 処理完了後にスピナーを消して別の内容を表示
        placeholder.empty()
        st.session_state.page = 'result'
        rerun()


def show_result():
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>診断結果</h1>", unsafe_allow_html=True)

    result_dict = st.session_state.answers
    result_val = result(result_dict)
    diagnosis_result = diagnosis_based_on_result(result_val)
    diagnosis_val = diagnosis_type(diagnosis_result)
    diagnosis_sentence = diagnosis_sentences(diagnosis_val)

    st.markdown(f"<p style='text-align: center; font-size:18px;'>あなたのタイプは...</p>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'>{diagnosis_val}</h3>", unsafe_allow_html=True)
    st.markdown(diagnosis_sentence, unsafe_allow_html=True)

    st.markdown("---")
    
    col1, col2, _ = st.columns([1,1,1])
    with col1:
        if st.button("🏠 スタート画面に戻る"):
            for k in ['questions', 'question_keys', 'current_q_idx', 'answers']:
                if k in st.session_state:
                    del st.session_state[k]
            st.session_state.page = 'top'
            st.rerun()
    with col2:
        if st.button("🔄 もう一度診断する"):
            for k in ['questions', 'question_keys', 'current_q_idx', 'answers']:
                if k in st.session_state:
                    del st.session_state[k]
            st.session_state.page = 'question_select'
            st.rerun()

# ページ遷移管理
if st.session_state.page == 'top':
    show_top()
elif st.session_state.page == 'example':
    show_example()
elif st.session_state.page == 'question_select':
    show_question_select()
elif st.session_state.page == 'loading':
    show_loading()
elif st.session_state.page == 'result':
    show_result()