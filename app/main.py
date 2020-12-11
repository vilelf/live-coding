import os

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from dotenv import load_dotenv

from app.routers import languages, topics

app = FastAPI()

load_dotenv(".env")

db_url = os.environ['DATABASE_URL']
app.add_middleware(DBSessionMiddleware, db_url=db_url)


@app.get('/', name='Ping')
async def root():
    return {'message': 'Pong'}


app.include_router(topics.router)
app.include_router(languages.router)