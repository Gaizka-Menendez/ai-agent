import os
from fastapi import FastAPI

app = FastAPI()

MY_PROJECT = os.environ.get("MY_PROJECT")
API_KEY = os.environ.get("API_KEY")
if not API_KEY or not MY_PROJECT:
    raise NotImplementedError("API_KEY or MY_PROJECT were not set properly")

@app.get("/")
def read_index():
    return {"hello": "world again", "Actual project": MY_PROJECT, "Api key": "elou"}