from pydantic import BaseModel
from typing import Optional


class ParentCreate(BaseModel):
    name: str
    phone_number:Optional[str]
    
class ParentResponseSchema(BaseModel):
    id: int
    name: str
    phone_number: Optional[str]

    class Config:
        from_attributes = True
