import streamlit as st
import base64

def render_home_logo():
    with open("Main/img/26287297.png", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <style>
        header, footer, div[data-testid="stToolbar"], div[data-testid="stDecoration"], header[data-testid="stHeader"] {{
            visibility: hidden;
            height: 0;
            position: fixed;
            pointer-events: none;
        }}
        .logo-button {{
            position: fixed;
            top: 10px;
            left: 10px;
            z-index: 1000;
            background: none;
            border: none;
            padding: 0;
        }}
        .logo-button img {{
            width: 100px;
            cursor: pointer;
            display: block;
        }}
        </style>

        <form action="?home_clicked=true" method="get">
            <button class="logo-button" type="submit">
                <img src="data:image/png;base64,{encoded}" alt="Home" />
            </button>
        </form>
    """, unsafe_allow_html=True)

    # クエリパラメータを監視
    query_params = st.query_params
    if query_params.get("home_clicked") == "true":
        st.session_state.page = "top"
        st.rerun()