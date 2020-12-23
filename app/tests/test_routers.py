import pytest
from fastapi_sqlalchemy import db, DBSessionMiddleware
from starlette.testclient import TestClient

from app import models
from app.crud.base import CRUDBase
from app.main import app


db_url = 'sqlite:///./test.db'

app.add_middleware(DBSessionMiddleware, db_url=db_url)
client = TestClient(app)

@pytest.fixture
def create_topic(request):
    with db():
        CRUDBase(models.Topic).create({'name': 'Python'})
    yield request


def test_ping():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Pong'}


def test_create_topic():
    response = client.post(
        '/topic/', 
        json={'name': 'asdf'}
    )
    assert response.status_code == 201
    assert response.json() == {'name': 'asdf'}


@pytest.mark.usefixtures('create_topic', 'tear_down')
def test_get_topics():
    response = client.get('/topics/')
    assert response.status_code == 200
    assert response.json() == [{'name': 'Python'}]


@pytest.mark.usefixtures('create_topic', 'tear_down')
def test_get_topic():
    response = client.get('/topic/1')
    assert response.status_code == 200
    assert response.json() == {'name': 'Python'}


def test_create_language():
    response = client.post(
        '/language/',
        json={'name': 'portuguese'}
    )

    assert response.status_code == 201
    assert response.json() == {'name': 'portuguese'}
