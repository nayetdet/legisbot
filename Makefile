.PHONY: api webui

api:
	uv run uvicorn packages.api.src.api.main:app --reload

webui:
	uv run streamlit run packages/webui/src/webui/main.py
