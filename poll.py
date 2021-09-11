from fastapi import FastAPI
from pydantic import BaseModel



app =  FastAPI()

class User(BaseModel):
    username: str
    email: str

class Poll(BaseModel):
    title: str
    type: str
    id_add_choices_active:bool
    is_voting_active:bool

@app.get('/')
async def home():
    return {'message': 'Great Biafra Land'}

@app.get('/polls')
async def polls():
    return {'polls': 'The Votes'}

@app.post('/polls')
async def polls():
    return {'polls': 'The Votes'}

@app.get('/users')
async def users():
    return {'users': 'List Of users'}

@app.post('/users')
async def users(user: User):
    return user