import streamlit as st
from rag import query_engine

def main():
    st.title("LegisBot")
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Insira uma pergunta"):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = query_engine.query(prompt)
            full_response = ""
            message_placeholder = st.empty()

            if hasattr(response, "source_nodes") and len(response.source_nodes) > 0:
                for chunk in response.response_gen:
                    full_response += chunk
                    message_placeholder.markdown(full_response + "▌")
            else: full_response = "Não encontrei base suficiente para responder com precisão."
            message_placeholder.markdown(full_response)
        st.session_state["messages"].append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
