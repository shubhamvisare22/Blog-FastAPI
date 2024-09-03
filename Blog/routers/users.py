from fastapi import APIRouter, Response
from schemas import  UserSchema
from utils import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from repository import users

router = APIRouter(
    prefix="/api/v1",
)


@router.post("/create_user", tags=['Users'])
def create_user(request: UserSchema, response: Response, db: Session = Depends(get_db)):
    return users.create(request, db, response)


@router.get("/list_users", tags=['Users'])
def list_users(response: Response, db: Session = Depends(get_db)):
    return users.list_users(db, response)


@router.get("/get_user/{user_id}", tags=['Users'])
def get_user(user_id: int, response: Response, db: Session = Depends(get_db)):
    return users.get(user_id, db, response)


@router.put("/update_user/{user_id}", tags=['Users'])
def update_user(user_id: int, request: UserSchema, response: Response, db: Session = Depends(get_db)):
    return users.update(user_id, request,db, response)


@router.delete("/delete_user/{user_id}", tags=['Users'])
def delete_user(user_id: int, response: Response, db: Session = Depends(get_db)):
    return users.destroy(user_id, db, response)
