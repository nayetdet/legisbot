from fastapi import APIRouter, FastAPI
from api.routes import dataset_route, qa_route

def register_routes(app: FastAPI) -> None:
    router = APIRouter(prefix="/v1")
    router.include_router(dataset_route.router, prefix="/datasets", tags=["Dataset"])
    router.include_router(qa_route.router, prefix="/qas", tags=["QA"])
    app.include_router(router)
