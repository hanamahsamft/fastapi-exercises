from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Class(SQLModel, table=True):
    __tablename__ = "classes"   
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    teacher_name: Optional[str] = None

    students: List["Student"] = Relationship(back_populates="classes")
