import uvicorn
import boto3
import json
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from utils.api import *
from utils.data.swimming import SWIMMING_DATA
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

@app.get("/swimming")
def football():
    
    return SWIMMING_DATA

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


@app.post('/queue')
async def add_to_queue(request : Request):
    
    message_data = json.loads(await request.body())
    
    sqs = boto3.client(
        'sqs',
        aws_access_key_id='ASIATUYJP7SUFPIUDPO6',
        aws_secret_access_key='0PoWcHVl7Id31UvTndvYiaewQYRdf9IY8QjgWLPE',
        aws_session_token='IQoJb3JpZ2luX2VjEGgaCXVzLWVhc3QtMSJHMEUCIQDTZzbVbtk32LUT+OcKGSCAipm6g0hP6uUSGd3E5NaElwIgWmzvjCffMk/cEirnCQjjY6nutzNh6a/dmTllkuIjDIMqhAQIoP//////////ARADGgwyNTA3Mzg2Mzc5OTIiDITg35fT7GT8EdrLYyrYA5IZEYEXFkmImsZZXVBNK46Fg5F4ghRmNkDikwgTPuTCqYdw9CNXIp1tMfs+JaTgASdB26TeP4HJMmdV3Nmaeo1GrFLARPLyqRdJfin6FfXoYuRN+DWig8HXp+U03R4Msoke1WdRYXZimwKaLQ5sM2uo6B+vgwMoOo8f2DSyijBDkjduTGTSUkw0YBgDQ7iuHN3Ok1vaw8PwmIgxdEmIAs5lOuKipyCA8rN2juZbu+Kkiv7BDvn27m/WwcOUXn7A4zbWeOL6cXUY0WVXXeXBfSe7rD7DSM2LyU/hQAHRxnj1VeYkdEmZ6JhnbN/uUCNiqKEtxReMRFb+F3Nr/ahkTOQpHmVD8Hh3YUC2x5PkUSspgxj1HsHjMeFPaQ0H2DjsNRu+Gs2Y8GAnUorwann8H5X5GNXah4Yks2i9TPp+sRQb4FVdEh41+CYsDE/OFr5Siq1xbGBEwouN4XDmF536HZLKCO1NgCHykoB72gy4rbyD0bUbiDfw7wMCdxumbrYCkognbLyRWg/7tloHUd83z+JIZ5FxoCzARn8C6UO7AY63nNGANYpTDkk4tO8e7sPlO72diV8hxXz9/b/aVIZWazfOOg6X2SUb6uJbFTOzkb1O/v129JSdDwEwv6PzsAY6pgGPbPpzGUIYADjLDxHz/lNEVOLZ/sbhYfU/3Zs46OPam2ST6LFsemb3pJCdmPwdVc6r6HolVLDdkg3EPsNMpnx0AW0DcEhXBEUCFQd9nocldME7lv/t7wJKbiQvKI9adKDRxehsU0iigiXr0ZZQo/ewk0AaDGNeAGMM6KN0qLMtY1h85DilQC1l+OQTsD1l4JHEU937aVNIArXsP55BE1ed6Ec+nhAF',
        region_name='eu-west-1'
    )
    
    queue_url = 'https://sqs.eu-west-1.amazonaws.com/250738637992/sport-player-ranking-queue'
    response = sqs.send_message(QueueUrl=queue_url,DelaySeconds=10, MessageBody=json.dumps(message_data))
    
    return {'messageid' : str(response['MessageId'])}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
