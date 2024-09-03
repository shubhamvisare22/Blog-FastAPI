from fastapi import APIRouter, Response
from schemas import BlogSchema, UserSchema
from utils import get_db
from repository import blogs
from fastapi import Depends
from sqlalchemy.orm import Session
from oauth2 import get_current_user

router = APIRouter(
    prefix="/api/v1",
)


@router.post("/create_blog", tags=['Blogs'])
def create_blog(response: Response, request: BlogSchema, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return blogs.create(request, db, response)


@router.get("/list_blog", tags=['Blogs'])
def list_blogs(response: Response, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return blogs.list_blogs(db, response)


@router.get("/get_blog/{id}", tags=['Blogs'])
def get_blog(response: Response, id: int, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return blogs.get(id, response, db)


@router.put("/update_blog/{id}", tags=['Blogs'])
def update_blog(response: Response, id: int, request: BlogSchema, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return blogs.update(id, db, request, response)


@router.delete("/delete_blog/{id}", tags=['Blogs'])
def delete_blog(response: Response, id: int, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return blogs.destroy(id, db, response)
