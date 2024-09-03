from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils import get_db
from repository import authentication
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return authentication.login_user(request, db)
