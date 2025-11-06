from fastapi import APIRouter, HTTPException
from models.parent import Parent
from schemas.parent import ParentResponseSchema,ParentCreate
from dependencies import SessionDep
router = APIRouter()

@router.post("/parents", response_model=ParentResponseSchema)
def create_parent(parents: ParentCreate, session: SessionDep)->dict:
    new_parent = Parent(
    name=parents.name,
    phone_number = parents.phone_number
)
    session.add(new_parent)
    session.commit()
    session.refresh(new_parent)
    return new_parent

@router.get("/parents/{parent_id}", response_model=ParentResponseSchema)
def get_parent(parent_id: int, session: SessionDep):
    parent_obj = session.get(Parent, parent_id)
    if not parent_obj:
        raise HTTPException(status_code=404, detail="Parent not found")
    return parent_obj
