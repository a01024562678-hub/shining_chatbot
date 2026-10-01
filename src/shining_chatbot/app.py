import streamlit as st

st.set_page_config(page_title="간단한 챗봇", page_icon="💬")
st.title("💬 간단한 챗봇")
st.caption("메시지를 입력하면 간단한 답변을 보여줘요.")

# 대화 내용을 저장해 두었다가 화면에 다시 표시합니다.
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    answer = f"안녕하세요! '{prompt}'라고 입력하셨네요. 반가워요!"
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
