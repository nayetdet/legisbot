.PHONY: api alembic-upgrade webui

api:
	uv run uvicorn packages.api.src.api.main:app --reload

alembic-upgrade:
	uv run alembic -c packages/api/alembic.ini upgrade head

webui:
	uv run streamlit run packages/webui/src/webui/main.py
