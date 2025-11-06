from pydantic import BaseModel
from typing import Optional


class ClassCreate(BaseModel):
    name:str
    teacher_name:str
    
    
class ClassResponseSchema(BaseModel):
    id: int
    name: str
    teacher_name: Optional[str]

    class Config:
        from_attributes = True
