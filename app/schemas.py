from typing import List
from pydantic import BaseModel


class Topic(BaseModel):
    name: str

    class Config:
        orm_mode = True



class Language(BaseModel):
    name: str

    class Config:
        orm_mode = True



class Streamer(BaseModel):
    name: str
    topics: List[Topic]
    languages: List[Language]

    class Config:
        orm_mode = True
