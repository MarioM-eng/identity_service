from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config.settings import get_config

DATABASE_URL = get_config().sqlmodel_database_uri

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """Dependency Injection para FastAPI que proporciona una sesión de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
