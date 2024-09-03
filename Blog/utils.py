from passlib.context import CryptContext
from database import SessionLocal

context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    try:
        return context.hash(password)
    except Exception as e:
        print(f"Error hashing password: {str(e)}")
        return None


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
        
def verify_password(plain_password, hashed_password):
    return context.verify(plain_password, hashed_password)
     


