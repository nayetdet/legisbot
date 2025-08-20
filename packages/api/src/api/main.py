from fastapi import FastAPI
from api.middlewares import register_middlewares

app = FastAPI()
register_middlewares(app)
