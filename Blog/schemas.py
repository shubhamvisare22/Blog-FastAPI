from pydantic import BaseModel


class BaseBlogSchema(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True


class BlogSchema(BaseBlogSchema):
    pass


class UserSchema(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        from_attributes = True
        
class LoginSchema(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True
        
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str
