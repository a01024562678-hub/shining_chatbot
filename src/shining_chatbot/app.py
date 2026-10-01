import os

import streamlit as st
from langchain.chat_models import init_chat_model

st.set_page_config(page_title="나의 첫 번째 챗봇", page_icon="💬", layout="wide")
st.title("💬 나의 첫 번째 챗봇")
st.write("Streamlit으로 만든 챗봇 페이지입니다.")


@st.cache_resource
def load_model(api_key):
    return init_chat_model(
        "gpt-6-luna",
        model_provider="openai",
        api_key=api_key,
    )


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    st.error("OPENAI_API_KEY가 설정되지 않았습니다. 환경 변수나 Streamlit secrets에 등록하세요.")
    st.stop()

model = load_model(api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("메시지를 입력하세요."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("답변을 만드는 중..."):
            try:
                answer = model.invoke(st.session_state.messages).content
                st.write(answer)
            except Exception as error:
                st.error(f"AI 응답을 가져오지 못했습니다: {error}")
                st.stop()

    st.session_state.messages.append({"role": "assistant", "content": answer})
