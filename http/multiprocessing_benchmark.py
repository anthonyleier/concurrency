from concurrent.futures import ProcessPoolExecutor
import os
import time
import requests
import multiprocessing


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


def processos():
    processos = []
    start = time.time()

    for i in range(1, 256):
        processo = multiprocessing.Process(target=gerar_pokemon, args=[i])
        processo.start()
        processos.append(processo)

    for processo in processos:
        processo.join()

    end = time.time()
    duracao = end - start
    print(f"Usando processos, a execução foi de {duracao} segundos")  # 97.90 segundos


def processos_pool_infinito():
    start = time.time()

    with ProcessPoolExecutor() as executor:
        executor.map(gerar_pokemon, range(1, 256))

    end = time.time()
    duracao = end - start
    print(f"Usando processos com pool (workers automáticos), a execução foi de {duracao} segundos")  # 80.87 segundos


def processos_pool_20():
    start = time.time()

    with ProcessPoolExecutor(max_workers=20) as executor:
        executor.map(gerar_pokemon, range(1, 256))

    end = time.time()
    duracao = end - start
    print(f"Usando processos com pool (20 workers), a execução foi de {duracao} segundos")  # 78.71 segundos


def processos_pool_10():
    start = time.time()

    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(gerar_pokemon, range(1, 256))

    end = time.time()
    duracao = end - start
    print(f"Usando processos com pool (10 workers), a execução foi de {duracao} segundos")  # 82.11 segundos


if __name__ == "__main__":
    esvaziar_pasta()
    processos()

    esvaziar_pasta()
    processos_pool_infinito()

    esvaziar_pasta()
    processos_pool_20()

    esvaziar_pasta()
    processos_pool_10()
