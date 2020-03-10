import logging
import sys
from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings
from loguru import logger

from core.logging import InterceptHandler

config = Config(".env")

MODEL = str = config(
    "MODEL", default="en_core_web_sm")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

PROJECT_NAME: str = config(
    "PROJECT_NAME", default="Axon Hackathon")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
