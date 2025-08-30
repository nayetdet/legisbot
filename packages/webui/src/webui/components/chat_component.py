import streamlit as st
from webui.mappers.qa_mapper import QAMapper
from webui.schemas.response.qa_response_schema import QAResponseSchema
from webui.services.qa_service import QAService

class ChatComponent:
    @staticmethod
    def render() -> None:
        st.title("LegisBot")
        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        for message in st.session_state["messages"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Insira uma pergunta:"):
            st.session_state["messages"].append({
                "content": prompt,
                "role": "user"
            })

            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                try:
                    response: QAResponseSchema = QAService.create(QAMapper.to_request(prompt))
                    st.markdown(response.answer)
                except Exception: st.error("Não encontrei base suficiente para responder com precisão.")
