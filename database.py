from sqlmodel import SQLModel, create_engine, Session
from typing import Generator


db_url = "postgresql://postgres:$7280Hhmrs@localhost:5432/school_db"

engine = create_engine(db_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator:
    with Session(engine) as session:
        yield session
