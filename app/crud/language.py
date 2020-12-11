from app.crud.base import CRUDBase
from app.models.language import Language


class CRUDLanguage(CRUDBase):
    def __init__(self):
        super().__init__(Language)
