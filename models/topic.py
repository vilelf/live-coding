from sqlalchemy import Column, String
from models.base import BaseModel


class Topic(BaseModel):
    __tablename__ = 'topic'

    name = Column(String, nullable=False)
