import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

    BASE_DIR = Path(__file__).resolve().parent.parent
    INSTANCE_DIR = BASE_DIR / "instance" / "database"
    INSTANCE_DIR.mkdir(parents=True, exist_ok=True)

    configured_database_url = os.getenv("DATABASE_URL", "").strip()
    if configured_database_url.startswith("sqlite:///"):
        relative_path = configured_database_url[len("sqlite:///"):]
        if relative_path and not relative_path.startswith("/"):
            relative_path = relative_path.lstrip("/")
            if relative_path.startswith("instance/"):
                relative_path = relative_path[len("instance/") :]
            if relative_path.startswith("database/"):
                relative_path = relative_path[len("database/") :]
            database_path = (INSTANCE_DIR / relative_path).resolve()
            database_path.parent.mkdir(parents=True, exist_ok=True)
            SQLALCHEMY_DATABASE_URI = f"sqlite:///{database_path}"
        else:
            SQLALCHEMY_DATABASE_URI = configured_database_url
    else:
        default_sqlite = f"sqlite:///{(INSTANCE_DIR / 'eshop.db').resolve()}"
        SQLALCHEMY_DATABASE_URI = configured_database_url or default_sqlite

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {"check_same_thread": False}
    } if SQLALCHEMY_DATABASE_URI.startswith("sqlite") else {}

