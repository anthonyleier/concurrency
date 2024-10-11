import os
import time
import requests
import threading
from concurrent.futures import ThreadPoolExecutor


def esvaziar_pasta():
    pasta = 'pokemons'
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        os.remove(caminho_arquivo)


def gerar_pokemon(id):
    nome, sprite = buscar_sprite(id)
    salvar_sprite(nome, sprite)


def buscar_sprite(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    response = requests.get(url)
    data = response.json()
    return data.get('species').get('name'), data.get('sprites').get('front_default')


def salvar_sprite(nome, sprite):
    response = requests.get(sprite)
    with open(f'pokemons/{nome}.png', 'wb') as arquivo:
        arquivo.write(response.content)


def threads():
    threads = []
    start = time.time()

    for i in range(1, 256):
        thread = threading.Thread(target=gerar_pokemon, args=[i])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end = time.time()
    duracao = end - start
    print(f"Usando threads, a execução foi de {duracao} segundos")  # 68.83 segundos


def threads_pool_infinito():
    start = time.time()

    with ThreadPoolExecutor() as executor:
        executor.map(gerar_pokemon, range(1, 256))

    end = time.time()
    duracao = end - start
    print(f"Usando threads com pool (workers automáticos), a execução foi de {duracao} segundos")  # 75.99 segundos


def threads_pool_20():
    start = time.time()

    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(gerar_pokemon, range(1, 256))

    end = time.time()
    duracao = end - start
    print(f"Usando threads com pool (20 workers), a execução foi de {duracao} segundos")  # 74.92 segundos


def threads_pool_10():
    start = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(gerar_pokemon, range(1, 256))

    end = time.time()
    duracao = end - start
    print(f"Usando threads com pool (10 workers), a execução foi de {duracao} segundos")  # 75.15 segundos


if __name__ == "__main__":
    esvaziar_pasta()
    threads()

    esvaziar_pasta()
    threads_pool_infinito()

    esvaziar_pasta()
    threads_pool_20()

    esvaziar_pasta()
    threads_pool_10()
