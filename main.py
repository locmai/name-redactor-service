import requests
import json
import spacy
import os


from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import ALLOWED_HOSTS, DEBUG, PROJECT_NAME

from api.router import router as api_router


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router)

    return application


app = get_application()
