from app.crud.base import CRUDBase
from fastapi import APIRouter

from app.schemas import Language
from app.crud.language import CRUDLanguage

router = APIRouter()


@router.post('/language/', response_model=Language, status_code=201)
def create_language(language: Language):
    return CRUDLanguage().create(language)
