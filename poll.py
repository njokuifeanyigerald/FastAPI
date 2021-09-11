from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import datetime



app =  FastAPI()

class User(BaseModel):
    username: str
    email: str
    # created_by:datetime.datetime
    # updated_by:datetime.datetime
   

class Poll(BaseModel):
    title: str
    type: str
    id_add_choices_active:bool
    is_voting_active:bool
    # created_by : Optional[str] = None
    created_by: int
    # created_at: datetime.datetime
    # updated_at: datetime.datetime

@app.get('/')
async def home():
    return {'message': 'Great Biafra Land'}

@app.get('/polls')
async def polls():
    return {'polls': 'The Votes'}

@app.post('/polls')
async def polls(poll: Poll):
    return poll
@app.get('/users')
async def users():
    return {'users': 'List Of users'}

@app.post('/users')
async def users(user: User):
    return user