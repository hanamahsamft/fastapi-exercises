from fastapi import FastAPI
from routers.classes import router as class_router
from routers.parent import router as parent_router
from routers.student import router as student_router

app = FastAPI()

app.include_router(class_router, tags=["Classes"])
app.include_router(parent_router, tags=["Parents"])
app.include_router(student_router, tags=["Students"])
