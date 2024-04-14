import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.api import *
from utils.data.football import FOOTBALL
from utils.data.chess import CHESS_DATA
from routes.cricket import cricket_router


origins = ["*"]

app = FastAPI()
app.include_router(cricket_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
def cricket():
    return {'Hello' : 'World'}


@app.get("/football")
def football():
    
    return FOOTBALL

@app.get("/chess")
def football():
    
    data = CHESS_DATA.get('results')
    newData = []
    
    for index, item in enumerate(data):
        player = {}
        player['name'] = item['fullname']
        player['nationality'] = item['country_abbr']
        player['rank'] = str(index+1)
        player['change'] = "0"
        newData.append(player)

    return newData

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
