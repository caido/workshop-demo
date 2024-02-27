from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api import demo_1


def create_app() -> FastAPI:
    app = FastAPI(title="Fastapi Template")

    app.mount("/static", StaticFiles(directory="static"), name="static")

    app.include_router(demo_1.router)

    origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
