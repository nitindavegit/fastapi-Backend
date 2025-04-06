from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from .import models
from .database import engine
from .routers import post, user, auth,vote
from .config import settings

#because i am using alembic to create table in db
#models.Base.metadata.create_all(bind = engine)

app = FastAPI()
  
  
origins = ["*"] # it means from every website, user can get API calls of our website


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
    
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message" : "Hello World. This is my API"}
