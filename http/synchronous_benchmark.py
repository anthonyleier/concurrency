import os
import time
import requests


def clear_folder():
    folder = 'pokemons'
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        os.remove(file_path)


def generate_pokemon(id):
    name, sprite = fetch_sprite(id)
    save_sprite(name, sprite)


def fetch_sprite(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    response = requests.get(url)
    data = response.json()
    return data.get('species').get('name'), data.get('sprites').get('front_default')


def save_sprite(name, sprite):
    response = requests.get(sprite)
    with open(f'pokemons/{name}.png', 'wb') as file:
        file.write(response.content)


def main():
    clear_folder()
    start = time.time()
    for i in range(1, 256):
        generate_pokemon(i)
    end = time.time()
    duration = end - start
    print(f"In synchronous approach, execution took {duration} seconds")  # 300.76 seconds


if __name__ == "__main__":
    main()
