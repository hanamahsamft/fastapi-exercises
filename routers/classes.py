from fastapi import APIRouter, HTTPException
from models.classes import Class
from schemas.classes import ClassResponseSchema,ClassCreate
from dependencies import SessionDep
router = APIRouter()

@router.post("/classes", response_model=ClassResponseSchema)
def create_class(classes: ClassCreate, session: SessionDep)->dict:
    new_class = Class(
    name=classes.name,
    teacher_name=classes.teacher_name
)
    session.add(new_class)
    session.commit()
    session.refresh(new_class)
    return new_class

@router.get("/classes/{class_id}", response_model=ClassResponseSchema)
def get_class(class_id: int, session: SessionDep):
    class_obj = session.get(Class, class_id)
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_obj

@router.delete("/classes/{class_id}")
def delete_class(class_id: int, session: SessionDep):
    class_obj = session.get(Class, class_id)
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    session.delete(class_obj)
    session.commit()
    return {"status": "success", "message": "Class deleted"}
