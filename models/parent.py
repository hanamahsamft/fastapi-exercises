from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Parent(SQLModel, table=True):
    __tablename__="parent"
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    phone_number: Optional[str] = None

    students: List["Student"] = Relationship(back_populates="parent")
