import os
import time
import asyncio
import aiohttp


def esvaziar_pasta():
    pasta = 'pokemons'
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        os.remove(caminho_arquivo)


async def gerar_pokemon(id, session):
    nome, sprite = await buscar_sprite(id, session)
    await salvar_sprite(nome, sprite, session)


async def buscar_sprite(id, session):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    async with session.get(url) as response:
        data = await response.json()
    return data.get('species').get('name'), data.get('sprites').get('front_default')


async def salvar_sprite(nome, sprite, session):
    async with session.get(sprite) as response:
        content = await response.read()
    if not os.path.exists('pokemons'):
        os.makedirs('pokemons')
    with open(f'pokemons/{nome}.png', 'wb') as arquivo:
        arquivo.write(content)


async def test_asyncio():
    async with aiohttp.ClientSession() as session:
        tasks = [gerar_pokemon(i, session) for i in range(1, 256)]
        start = time.time()
        await asyncio.gather(*tasks)
        end = time.time()
        duracao = end - start
        print(f"Com asyncio, a execução foi de {duracao} segundos") # 2.01 segundos


if __name__ == "__main__":
    esvaziar_pasta()
    asyncio.run(test_asyncio())
