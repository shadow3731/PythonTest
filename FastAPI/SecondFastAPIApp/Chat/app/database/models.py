from .configuration import Base

from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Boolean, 
    DateTime, 
    ForeignKey,
)
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    login = Column(String, index=True)
    hashed_password = Column(String, index=True)
    registered_at = Column(DateTime)
    banned = Column(Boolean, index=True, default=False)
    
    messages = relationship('Message', back_populates='user')
    
class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True)
    text = Column(String, index=True)
    posted_at = Column(DateTime, index=True)
    deleted = Column(Boolean, index=True, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='messages')