import os
from fastapi import FastAPI
from api.db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app starts
    init_db() # we make sure the db is already up before starting the app
    yield
    # after app startup

app = FastAPI(lifespan=lifespan)

# MY_PROJECT = os.environ.get("MY_PROJECT") or "This is my project"
# API_KEY = os.environ.get("API_KEY")
# if not API_KEY or not MY_PROJECT:
#     raise NotImplementedError("API_KEY or MY_PROJECT were not set properly")

@app.get("/")
def read_index():
    return {"hello": "world again"}

@app.get("/health")
def health_check():
    return {"status": "Everything ok"}