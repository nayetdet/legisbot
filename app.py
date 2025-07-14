import streamlit as st
import time
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

        response = query_engine.query(prompt)
        full_response = ""

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            for i in range(5):
                response_placeholder.markdown(f"{'.' * (i % 4)}")
                time.sleep(0.3)

            for chunk in response.response_gen:
                full_response += chunk
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)

        st.session_state["messages"].append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
