FROM ollama/ollama:latest
RUN nohup bash -c "ollama serve &" && \
    sleep 5 && \
    ollama pull deepseek-r1:1.5b && \
    ollama pull qwen:0.5b
