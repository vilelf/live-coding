from sqlalchemy import Column, String
from app.models.base import BaseModel


class Language(BaseModel):
    name = Column(String, nullable=False)
    icon = Column(String)
