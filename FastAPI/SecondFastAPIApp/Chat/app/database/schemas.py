import datetime

from pydantic import BaseModel


class MessageBase(BaseModel):
    text: str
    posted_at: datetime
    deleted: bool
    
class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    user_id: int
    
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    login: str
    registered_at: datetime
    
    class Config:
        orm_mode = True
    
class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    banned: bool
    
    messages: list[Message] = []