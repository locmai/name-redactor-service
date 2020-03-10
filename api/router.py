from api import redactor, health

from fastapi import APIRouter


router = APIRouter()

router.include_router(redactor.router, tags=["redactor"])

router.include_router(health.router, tags=["health"])
