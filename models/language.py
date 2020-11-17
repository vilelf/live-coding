from sqlalchemy import Column, String
from models.base import BaseModel


class Language(BaseModel):
    __tablename__ = 'language'

    name = Column(String, nullable=False)
    icon = Column(String)
