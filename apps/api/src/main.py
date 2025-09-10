from fastapi import FastAPI
from .api import search

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(search.router)