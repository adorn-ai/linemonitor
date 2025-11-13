from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

if settings.APP_ENV == "prod":
    engine = create_engine(settings.AIVEN_URL, pool_pre_ping=True)
else:
    engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
