from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class Base:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


BaseModel = declarative_base(cls=Base)
