from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.backend.presentation.endpoints import api_router

from .settings import settings


def create_fastapi_app(settings=settings):
    app = FastAPI(title="Biofood API")

    app.include_router(api_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOW_ORIGINS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )
    return app


app = create_fastapi_app()
