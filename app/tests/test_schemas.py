from app.schemas import Topic, Language, Streamer


def test_topic():
    topic = Topic(name='python')
    assert topic.name == 'python'


def test_language():
    language = Language(name='english')
    assert language.name == 'english'

def test_streamer():
    streamer = Streamer(
        name='vilelf',
        topics=[
            Topic(name='python'),
            Topic(name='fastapi')
        ],
        languages=[
            Language(name='portuguese')
        ]
    )
    assert streamer.dict() == {
        'name': 'vilelf',
        'topics': [
            {'name': 'python'}, 
            {'name': 'fastapi'}
        ],
        'languages': [
            {'name': 'portuguese'}
        ]
    }
