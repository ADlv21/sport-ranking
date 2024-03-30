import uvicorn
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.api import *
from routes.cricket import cricket_router


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "*"
]

app = FastAPI()
app.include_router(cricket_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def cricket():
    return {'Hello' : 'World'}


@app.get("/football")
def football():
    response = requests.get(FOOTBALL_URL)
    data = response.json()['sheets']['players']
    new_data = []
    
    for item in data:
        new_item = {
            "name": item["Name"],
            "change": item["Up or down"],
            "nationality": item["Nationality"],
            "rank": item["Rank"]
        }
        new_data.append(new_item)
    
    return new_data

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
