from sqlalchemy import Column, String
from models.base import BaseModel


class Topic(BaseModel):
    __tablename__ = 'topic'

    name = Column(String)

    def __init__(self, name) -> None:
        self.name = name
