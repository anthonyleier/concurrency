import os
import time
import requests
import threading
from concurrent.futures import ThreadPoolExecutor


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


def threads():
    threads = []
    start = time.time()

    for i in range(1, 256):
        thread = threading.Thread(target=generate_pokemon, args=[i])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end = time.time()
    duration = end - start
    print(f"Using threads, execution took {duration} seconds")


def threads_pool_default_workers():
    start = time.time()

    with ThreadPoolExecutor() as executor:
        executor.map(generate_pokemon, range(1, 256))

    end = time.time()
    duration = end - start
    print(f"Using threads with pool (default workers), execution took {duration} seconds")


def threads_pool_20_workers():
    start = time.time()

    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(generate_pokemon, range(1, 256))

    end = time.time()
    duration = end - start
    print(f"Using threads with pool (20 workers), execution took {duration} seconds")


def threads_pool_10_workers():
    start = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(generate_pokemon, range(1, 256))

    end = time.time()
    duration = end - start
    print(f"Using threads with pool (10 workers), execution took {duration} seconds")


if __name__ == "__main__":
    clear_folder()
    threads()

    clear_folder()
    threads_pool_default_workers()

    clear_folder()
    threads_pool_20_workers()

    clear_folder()
    threads_pool_10_workers()
