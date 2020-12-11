from typing import List

from fastapi import APIRouter

from app.crud.topic import CRUDTopic
from app.schemas import Topic as TopicSchema


router = APIRouter()


@router.get('/topics/', response_model=List[TopicSchema])
def get_topics():
    return CRUDTopic().all()


@router.post('/topic/', response_model=TopicSchema, status_code=201)
def create_topic(topic: TopicSchema):
    return CRUDTopic().create(topic)


@router.get('/topic/{topic_id}', response_model=TopicSchema)
def get_topic(topic_id: int):
    crud_topic = CRUDTopic()
    return crud_topic.get(topic_id)
