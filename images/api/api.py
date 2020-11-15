from typing import Optional
from fastapi import FastAPI
import db as db

app = FastAPI()

conn = db.connect()

@app.get("/")
async def root(name: Optional[str] = "World"):
    return {'greeting': 'Hello', 'name': name}
