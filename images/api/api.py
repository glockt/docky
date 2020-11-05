from typing import Optional
from fastapi import FastAPI
from waitress import serve

app = FastAPI()

@app.get("/")
async def root(name: Optional[str] = "World"):
    return {'greeting': 'Hello', 'name': name}

#Create the main driver function
if __name__ == '__main__':
    #call the run method
    serve(app, host="0.0.0.0", port=8081)
