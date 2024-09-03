from datetime import datetime, timedelta, timezone
from schemas import TokenData
from jwt.exceptions import InvalidTokenError
import jwt
import os 
from dotenv import load_dotenv
load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY') 
ALGORITHM = os.getenv('ALGORITHM') 
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES') 


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode["exp"] = expire
    return {"access_token":jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM), "token_type":"bearer"}


def verify_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        return TokenData(username=username)
    except InvalidTokenError as e:
        raise credentials_exception from e 