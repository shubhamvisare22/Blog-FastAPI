from fastapi import Response, status
from sqlalchemy.orm import Session
from models import Blog


def create(request, db: Session, response: Response):
    try:
        new_blog = Blog(title=request.title, content=request.content, user_id=1)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        response.status_code = status.HTTP_201_CREATED
        return {"status": True, "data": new_blog}
    except Exception as e:
        db.rollback()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "msg": str(e)}


def list_blogs(db: Session, response: Response):
    try:
        blogs = db.query(Blog).all()
        response.status_code = status.HTTP_200_OK
        return {"status": True, "data": blogs}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "msg": str(e)}


def get(id: int, response: Response, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status": False, "msg": "Blog not found"}
    
    response.status_code = status.HTTP_200_OK
    return {"status": True, "data": blog}


def update(id: int, db: Session, request, response: Response):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status": False, "msg": "Blog not found"}

    try:
        blog.title = request.title
        blog.content = request.content
        db.commit()
        response.status_code = status.HTTP_200_OK
        return {"status": True, "data": blog}
    except Exception as e:
        db.rollback()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "msg": str(e)}


def destroy(id: int, db: Session, response: Response):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status": False, "msg": "Blog not found"}
    
    try:
        db.delete(blog)
        db.commit()
        response.status_code = status.HTTP_200_OK
        return {"status": True, "msg": "Blog deleted successfully"}
    except Exception as e:
        db.rollback()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": False, "msg": str(e)}
