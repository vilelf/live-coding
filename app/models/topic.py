from sqlalchemy import Column, String
from app.models.base import BaseModel


class Topic(BaseModel):
    name = Column(String, nullable=False)
