from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    chat_id = Column(Integer, unique=True)
    created_at = Column(DateTime)

    def __init__(self, username, chat_id, created_at):
        self.username = username
        self.chat_id = chat_id
        self.created_at = created_at