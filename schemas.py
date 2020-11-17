from typing import List
from pydantic import BaseModel


class ProgrammingLanguage(BaseModel):
    name: str


class SpokenLanguage(BaseModel):
    name: str


class Streamer(BaseModel):
    name: str
    programming_languages: List[ProgrammingLanguage]
    spoken_languages: List[SpokenLanguage]
