import pytest
from fastapi_sqlalchemy import db

from app import models
from app.crud.topic import CRUDTopic
from app.schemas import Topic as TopicSchema


def drop_tables():
    with db():
        db.session.query(models.Streamer).delete()
        db.session.query(models.Language).delete()
        db.session.query(models.Topic).delete()
        db.session.commit()


@pytest.fixture(autouse=True)
def tear_down(request):
    yield request
    drop_tables()


@pytest.fixture
def create_topic_dummy():
    topic = TopicSchema(name='topic_xpto')
    with db():
        CRUDTopic().create(topic)
