from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional
from schemas.classes import ClassResponseSchema
from schemas.parent import ParentResponseSchema

class StudentCreateSchema(BaseModel):
    name: str
    age: int
    grade: int
    class_id: int
    parent_id: int

    @validator("age")
    def check_age(cls, v):
        if v < 6:
            raise ValueError("student too young for registration")
        return v


class StudentResponseSchema(BaseModel):
    id: int
    name: str
    age: int
    grade: int
    is_active: bool
    created_at: datetime
    class_: Optional[ClassResponseSchema]
    parent: Optional[ParentResponseSchema]

    class Config:
        from_attributes = True
