from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import dotenv
import os

dotenv.load_dotenv()

DATABASE_URL = os.getenv('BREAL_SUPABASE_URL')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()