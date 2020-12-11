import pytest
from fastapi_sqlalchemy import db, DBSessionMiddleware

from app.crud.topic import CRUDTopic
from app.main import app
from app.models.topic import Topic


db_url = 'sqlite:///./test.db'

app.add_middleware(DBSessionMiddleware, db_url=db_url)


@pytest.mark.usefixtures('create_topic_dummy', 'tear_down')
def test_get__model_returns_a_model_instance():
    crud = CRUDTopic()
    with db():
        result = crud.get(1)
    assert isinstance(result, Topic)


@pytest.mark.usefixtures('create_topic_dummy', 'tear_down')
def test_get__model_attr_is_the_same_created_by_fixture():
    crud = CRUDTopic()
    with db():
        result = crud.get(1)
    assert result.name == 'topic_xpto'
