import os
import time
import requests
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


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


def processes():
    processes = []
    start = time.time()

    for i in range(1, 256):
        process = multiprocessing.Process(target=generate_pokemon, args=[i])
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end = time.time()
    duration = end - start
    print(f"Using processes, execution took {duration} seconds")  # 97.90 seconds


def processes_pool_default_workers():
    start = time.time()

    with ProcessPoolExecutor() as executor:
        executor.map(generate_pokemon, range(1, 256))

    end = time.time()
    duration = end - start
    print(f"Using process pool (default workers), execution took {duration} seconds")  # 80.87 seconds


def processes_pool_20_workers():
    start = time.time()

    with ProcessPoolExecutor(max_workers=20) as executor:
        executor.map(generate_pokemon, range(1, 256))

    end = time.time()
    duration = end - start
    print(f"Using process pool (20 workers), execution took {duration} seconds")  # 78.71 seconds


def processes_pool_10_workers():
    start = time.time()

    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(generate_pokemon, range(1, 256))

    end = time.time()
    duration = end - start
    print(f"Using process pool (10 workers), execution took {duration} seconds")  # 82.11 seconds


if __name__ == "__main__":
    clear_folder()
    processes()

    clear_folder()
    processes_pool_default_workers()

    clear_folder()
    processes_pool_20_workers()

    clear_folder()
    processes_pool_10_workers()
