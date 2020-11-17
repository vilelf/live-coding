from sqlalchemy import Column, String
from models.base import BaseModel


class Language(BaseModel):
    __tablename__ = 'language'

    name = Column(String)
    icon = Column(String)

    def __init__(self, name, icon) -> None:
        self.name = name
        self.icon = icon
