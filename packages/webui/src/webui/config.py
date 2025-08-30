from os import getenv

class Config:
    WEBUI_API_URL: str = getenv("WEBUI_API_URL")
