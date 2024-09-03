from sqlalchemy.orm import Session
from fastapi import status, Response
from models import User
from utils import hash_password


def create(request, db: Session, response: Response):
    try:
        new_user = User(username=request.username, password=hash_password(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        response.status_code = status.HTTP_201_CREATED
        return {"status": True, "data": new_user}
    except Exception as e:
        db.rollback()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "msg": str(e)}


def list_users(db: Session, response: Response):
    try:
        users = db.query(User).all()
        response.status_code = status.HTTP_200_OK
        return {"status": True, "data": users}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "msg": str(e)}


def get(user_id: int, db: Session, response: Response):
    try:
        user = db.query(User).get(user_id)
        if not user:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"status": False, "msg": "User not found"}
        
        response.status_code = status.HTTP_200_OK
        return {"status": True, "data": user}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "msg": str(e)}


def update(user_id: int, request, db: Session, response: Response):
    try:
        user = db.query(User).get(user_id)
        if not user:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"status": False, "msg": "User not found"}

        user.username = request.username
        if request.password:
            user.password = hash_password(request.password)
        db.commit()
        db.refresh(user)
        response.status_code = status.HTTP_200_OK
        return {"status": True, "data": user}
    except Exception as e:
        db.rollback()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "msg": str(e)}


def destroy(user_id: int, db: Session, response: Response):
    try:
        user = db.query(User).get(user_id)
        if not user:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"status": False, "msg": "User not found"}
        
        db.delete(user)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return {"status": True, "msg": "User deleted successfully"}
    except Exception as e:
        db.rollback()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "msg": str(e)}
