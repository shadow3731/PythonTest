from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DB_URL = "mysql://root:admin@localhost/second_fastapi_app_db"

engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine,
)

Base = declarative_base()