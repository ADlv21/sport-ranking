import uvicorn
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.api import *

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://127.0.0.1:3000"
]

app = FastAPI()

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

@app.get("/cricket-allrounder-odi")
def cricket():
    response = requests.get(ODI_ALLROUNDER_CRICKET_URL)
    data = response.json()['data']['bat-rank']['rank']
    
    new_data = []
    for item in data:
        new_item = {
            "name": item["Player-name"],
            "change": item["change"],
            "nationality": item["Country_name"],
            "rank": item["no"]
        }
        new_data.append(new_item)
    
    return new_data

@app.get("/cricket-allrounder-test")
def cricket():
    response = requests.get(TEST_ALLROUNDER_CRICKET_URL)
    data = response.json()['data']['bat-rank']['rank']
    
    new_data = []
    for item in data:
        new_item = {
            "name": item["Player-name"],
            "change": item["change"],
            "nationality": item["Country_name"],
            "rank": item["no"]
        }
        new_data.append(new_item)
    
    return new_data

@app.get("/cricket-allrounder-t20")
def cricket():
    response = requests.get(T20_ALLROUNDER_CRICKET_URL)
    data = response.json()['data']['bat-rank']['rank']
    new_data = []
    for item in data:
        new_item = {
            "name": item["Player-name"],
            "change": item["change"],
            "nationality": item["Country_name"],
            "rank": item["no"]
        }
        new_data.append(new_item)
    
    return new_data
    

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
