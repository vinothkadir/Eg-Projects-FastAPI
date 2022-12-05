from fastapi import FastAPI, Depends 
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .database import engine, get_db
from sqlalchemy.orm import Session
from .import models
from .routers import users, post, auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
print(settings.database_username)

#models.Base.metadata.create_all(bind=engine)
app = FastAPI()
#origins = ["https://www.google.com/"]
origins = ["*"] # this allows all domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#while True:
#  try:
#      conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Vinoth9591asdqaz', cursor_factory=RealDictCursor)
#      cursor = conn.cursor()
#      print('Database connection was successful')
#      break
#   except Exception as error:
#      print('connection to database is failed')
#      print('error:',error)
#      time.sleep(1)
#my_posts = [{"title": "title of posts 1","content": "content of table 1", "id":1},{
#   "title": "favorite foods", "content":"i like pizza", "id":2}]
#def find_post(id):
#   for p in my_posts:
#      if p["id"] == id:
#         return p
#def find_index_post(id):
#   for i, q in enumerate(my_posts):
#      if q['id'] == id:
#         return i  
app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)
#@app.get("/") 
#def root():
#   return {"message": "Hello World!!"}
#@app.get("/sqlalchemy")
#def test_posts(db: Session = Depends(get_db)):
#   posts = db.query(models.Post).all()
#   return posts




