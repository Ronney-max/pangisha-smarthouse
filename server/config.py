import os
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


def _is_local_placeholder_database_url(database_url: str) -> bool:
    if not database_url:
        return True

    parsed = urlparse(database_url)
    host = (parsed.hostname or "").lower()
    username = (parsed.username or "").lower()
    password = (parsed.password or "").lower()

    return (
        parsed.scheme in {"postgresql", "postgres", "postgresql+psycopg2"}
        and host in {"localhost", "127.0.0.1"}
        and username in {"postgres", ""}
        and password in {"password", "postgres", ""}
    )


class Config:
    database_url = os.environ.get("DATABASE_URL", "").strip()

    if database_url and database_url.startswith("sqlite://"):
        parsed = urlparse(database_url)
        sqlite_path = parsed.path or "pangisha-dev.db"
        if not os.path.isabs(sqlite_path):
            instance_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "instance"))
            os.makedirs(instance_dir, exist_ok=True)
            sqlite_path = os.path.join(instance_dir, sqlite_path)
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{sqlite_path}"
    elif database_url and database_url.startswith(("postgresql://", "postgres://", "postgresql+psycopg2://")) and not _is_local_placeholder_database_url(database_url):
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        instance_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "instance"))
        os.makedirs(instance_dir, exist_ok=True)
        db_path = os.path.join(instance_dir, "pangisha-dev.db")
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")