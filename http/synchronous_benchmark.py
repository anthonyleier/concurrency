import os
import time
import requests


def esvaziar_pasta():
    pasta = 'pokemons'
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        os.remove(caminho_arquivo)


def gerar_pokemon(id):
    print(f"Processando pokemon {id}")
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


def puro():
    esvaziar_pasta()
    start = time.time()
    for i in range(1, 256):
        gerar_pokemon(i)
    end = time.time()
    duracao = end - start
    print(f"Em Python Puro, a execução foi de {duracao} segundos")  # 300.76 segundos


if __name__ == "__main__":
    puro()
