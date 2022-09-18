from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,Union



app=FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None]=None


@app.get("/")
def read_root():
    return {'data':'blog list'}

@app.get("/blog")
def get_blog(limit:int=10,unpublished:bool=False, sort:Optional[str] = None):
    if unpublished:
        return {'data':f'{limit} unpublished blogs from the db '}
    return {'data':f'{limit} published blogs from the db'}

@app.get('/blog/unpublished')
def unpublished(id:int):
    return {'unpublished':True}

@app.get('/blog/{id}')
def show_item(id:int ):
    return {'data ':id}

@app.get('/blog/{id}/comments')
def show_item(id:int):
    return {'data':{'comments':id}}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]



@app.post('/blog')
def create_blog(request:Blog):
    return {'data':"Blog is created"} 
