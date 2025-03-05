from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.backend.presentation.endpoints.auth import auth_router
from src.backend.presentation.endpoints.categories import categories_router
from src.backend.presentation.endpoints.dishes import dishes_router
from src.backend.presentation.endpoints.orders.routes import orders_router
from src.backend.presentation.endpoints.shopping_cart import shopping_cart_router

from .settings import settings


def create_fastapi_app(settings=settings):
    app = FastAPI(title="Biofood API")
    api_router = APIRouter(prefix="/api")
    add_endpoints(api_router)

    app.include_router(api_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOW_ORIGINS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )
    return app


def add_endpoints(api_router: APIRouter):
    api_router.include_router(auth_router)
    api_router.include_router(categories_router)
    api_router.include_router(dishes_router)
    api_router.include_router(orders_router)
    api_router.include_router(shopping_cart_router)


app = create_fastapi_app()
