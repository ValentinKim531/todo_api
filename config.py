import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


POSTGRES_DB = os.getenv("POSTGRES_DB", "todo")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")

TECHPARK_URL = os.getenv(
    "TECHPARK_URL", "https://astanahub.com/ru/service/techpark/"
)
TECHPARK_TIMEOUT = int(os.getenv("TECHPARK_TIMEOUT", "60000"))


DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-dev-key")
DJANGO_DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() in (
    "true",
    "1",
    "yes",
)
DJANGO_ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost").split(
    ","
)
