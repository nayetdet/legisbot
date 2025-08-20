from fastapi import FastAPI
from api.middlewares.cors_middleware import register_cors_middleware

def register_middlewares(app: FastAPI):
    register_cors_middleware(app)
