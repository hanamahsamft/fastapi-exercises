from fastapi import APIRouter,HTTPException
from sqlmodel import Session, select
from models.student import Student
from models.classes import Class
from models.parent import Parent
from schemas.student import StudentCreateSchema, StudentResponseSchema
from dependencies import SessionDep

router = APIRouter()

def validate_class_and_parent(class_id: int, parent_id: int, session: Session):
    class_obj = session.get(Class, class_id)
    parent_obj = session.get(Parent, parent_id)
    if not class_obj or not parent_obj:
        raise HTTPException(status_code=400, detail="class or parent not found")
    return class_obj, parent_obj

@router.post("/students", response_model=StudentResponseSchema)
def create_student(students: StudentCreateSchema, session: SessionDep):
    class_obj, parent_obj = validate_class_and_parent(students.class_id, students.parent_id, session)
    
    class_exists = session.query(Class).filter(Class.id == students.class_id).first()  
    if not class_exists:
        raise HTTPException(status_code=400, detail="Class not found")

    student = Student(**students.dict())
    session.add(student)
    session.commit()
    session.refresh(student)
    return StudentResponseSchema(
        id=student.id,
        name=student.name,
        age=student.age,
        grade=student.grade,
        is_active=student.is_active,
        created_at=student.created_at,
        class_=class_obj,
        parent=parent_obj
    )

@router.get("/students/{student_id}", response_model=StudentResponseSchema)
def get_student(student_id: int, session: SessionDep):
    statement = (
        select(Student, Class, Parent)
        .join(Class, Student.class_id == Class.id)
        .join(Parent, Student.parent_id == Parent.id)
        .where(Student.id == student_id)
    )
    result = session.exec(statement).first()
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")

    student, class_obj, parent_obj = result

    return StudentResponseSchema(
        id=student.id,
        name=student.name,
        age=student.age,
        grade=student.grade,
        is_active=student.is_active,
        created_at=student.created_at,
        class_=class_obj,
        parent=parent_obj
    )
