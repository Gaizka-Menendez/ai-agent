import os
from fastapi import FastAPI
from api.db import init_db
from contextlib import asynccontextmanager

from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app starts
    init_db() # we make sure the db is already up before starting the app
    yield
    # after app startup

app = FastAPI(lifespan=lifespan)

# esta línea lo que permite es añadir routers, de forma que todo lo que tenga que ver con chats se encuentre en la ruta api/chats
# Mantiene la aplicación modular y ordenada además de permitirnos reutilizar y escalar
app.include_router(chat_router, prefix="/api/chats")

@app.get("/")
def read_index():
    return {"hello": "world again"}

@app.get("/health")
def health_check():
    return {"status": "Everything ok"}