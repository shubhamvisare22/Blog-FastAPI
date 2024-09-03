from models import User
from sqlalchemy.orm import Session
from utils import verify_password
from repository.token import create_access_token


def login_user(request, db: Session):
    user_obj = db.query(User).filter(User.username == request.username).first()

    if not user_obj:
        return {"status": False, "msg": "User not found"}

    elif not verify_password(request.password, user_obj.password):
        return {"status": False, "msg": "Inccorrect password"}

    else:
        return create_access_token({"sub": request.username})
