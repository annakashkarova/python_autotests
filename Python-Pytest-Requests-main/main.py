import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '109927964a0f8bf9b327200240c3d21b'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

# Создание нового покемона
body_new = {
    "name": "generate",
    "photo_id": -1
}

# Запрос на создание покемона
response_creat = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_new)
print(f"Создание покемона: {response_creat.text}")
print(f"Статус ответа на создание покемона: {response_creat.status_code}")

# Проверяем успешность запроса (201)
if response_creat.status_code in [201]:
    pokemon_id = response_creat.json().get('id')
    print(f"Создан покемон с ID: {pokemon_id}")

    # Изменение имени покемона 
    body_newname = {
        "pokemon_id": pokemon_id,
        "name": "generate",
        "photo_id": -1
    }

    response_newname = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_newname)
    print(f"Изменение имени покемона: {response_newname.text}")
    print(f"Статус ответа на изменение имени покемона: {response_newname.status_code}")

    # Добавление покемона в покебол
    body_pokeball = {
        "pokemon_id": pokemon_id
    }

    response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
    print(f"Добавление покемона в покебол: {response_pokeball.text}")
    print(f"Статус ответа на добавление покемона в покебол: {response_pokeball.status_code}")

else:
    print(f"Ошибка при создании покемона: {response_creat.text}")
    print(f"Статус ошибки создания покемона: {response_creat.status_code}")
