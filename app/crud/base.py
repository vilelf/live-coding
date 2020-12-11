from typing import Generic, Type, TypeVar

import pydantic
from fastapi.encoders import jsonable_encoder
from fastapi_sqlalchemy import db

from app.models.base import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=pydantic.BaseModel)

class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, model_id: int):
        return db.session.query(self.model).filter(self.model.id == model_id).one() 

    def create(self, obj_in: CreateSchemaType):
        obj_in_data = jsonable_encoder(obj_in)
        obj = self.model(**obj_in_data)
        db.session.add(obj)
        db.session.commit()
        return obj

    def all(self):
        return db.session.query(self.model).all()
