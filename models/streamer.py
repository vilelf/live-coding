from sqlalchemy import Column, String

from models.base import BaseModel


class Streamer(BaseModel):
    __tablename__ = 'streamer'

    name = Column(String, nullable=False)
