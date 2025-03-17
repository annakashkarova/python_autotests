import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '109927964a0f8bf9b327200240c3d21b'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '22990'

def test_status_code() :
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response_get.json()["data"][0]["trainer_name"] == 'Cousteau'