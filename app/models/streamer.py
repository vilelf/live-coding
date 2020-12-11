from sqlalchemy import Column, String

from app.models.base import BaseModel


class Streamer(BaseModel):
    name = Column(String, nullable=False)
