FROM ollama/ollama:latest
ARG OLLAMA_LLM_MODEL
ARG OLLAMA_EMBEDDING_MODEL
RUN nohup bash -c "ollama serve &" && \
    sleep 5 && \
    ollama pull "${OLLAMA_LLM_MODEL}" && \
    ollama pull "${OLLAMA_EMBEDDING_MODEL}" \
