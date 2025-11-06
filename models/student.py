from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List
from models.parent import Parent
from models.classes import Class
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.classes import Class
    from models.parent import Parent


class Student(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    age: int
    grade: int
    class_id: int = Field(foreign_key="classes.id") 
    parent_id: int = Field(foreign_key="parent.id")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    classes: Optional[Class] = Relationship(back_populates="students")
    parent: Optional[Parent] = Relationship(back_populates="students")

    