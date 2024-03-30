import requests
from fastapi import APIRouter
from utils.api import *


cricket_router = APIRouter()

@cricket_router.get("/cricket-allrounder-odi")
def cricketallodi():
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

@cricket_router.get("/cricket-allrounder-test")
def cricketalltest():
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

@cricket_router.get("/cricket-allrounder-t20")
def cricketallt20():
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
    




# ===========================================================================
@cricket_router.get("/cricket-bowl-odi")
def cricketbowlodi():
    response = requests.get(ODI_BOWLING_CRICKET_URL)
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

@cricket_router.get("/cricket-bowl-test")
def cricketbowltest():
    response = requests.get(TEST_BOWLING_CRICKET_URL)
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

@cricket_router.get("/cricket-bowl-t20")
def cricketbowlt20():
    response = requests.get(T20_BOWLING_CRICKET_URL)
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

# ===============================================================================



@cricket_router.get("/cricket-bat-odi")
def cricketbatodi():
    response = requests.get(ODI_BATTING_CRICKET_URL)
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

@cricket_router.get("/cricket-bat-test")
def cricketbattest():
    response = requests.get(TEST_BATTING_CRICKET_URL)
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

@cricket_router.get("/cricket-bat-t20")
def cricketbatt20():
    response = requests.get(T20_BATTING_CRICKET_URL)
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

