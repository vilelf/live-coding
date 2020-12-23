from app.crud.base import CRUDBase
from app.models import Topic

class CRUDTopic(CRUDBase):
    def __init__(self):
        super().__init__(Topic)
