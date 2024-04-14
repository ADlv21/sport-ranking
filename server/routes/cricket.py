import requests
from fastapi import APIRouter
from utils.api import *
from utils.data.cricket import *

cricket_router = APIRouter()

@cricket_router.get("/cricket-allrounder-odi")
def cricketallodi():
    
    return cricketAllrounderOdi

@cricket_router.get("/cricket-allrounder-test")
def cricketalltest():
    
    return cricketAllrounderTest

@cricket_router.get("/cricket-allrounder-t20")
def cricketallt20():
    
    return cricketAllrounderT20


# ===========================================================================
@cricket_router.get("/cricket-bowl-odi")
def cricketbowlodi():
    
    return cricketBowlOdi

@cricket_router.get("/cricket-bowl-test")
def cricketbowltest():
    
    return cricketBowlTest

@cricket_router.get("/cricket-bowl-t20")
def cricketbowlt20():
    
    return cricketBowlT20

# ===============================================================================

@cricket_router.get("/cricket-bat-odi")
def cricketbatodi():
    
    return cricketBatOdi

@cricket_router.get("/cricket-bat-test")
def cricketbattest():
    
    return cricketBatTest

@cricket_router.get("/cricket-bat-t20")
def cricketbatt20():
    return cricketBatT20

