from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv

load_dotenv()
engine = create_engine('sqlite:///process.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def yield_db() -> Session:
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
