import os
import time
import asyncio
import aiohttp


def clear_folder():
    folder = 'pokemons'
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        os.remove(file_path)


async def generate_pokemon(id, session):
    name, sprite = await fetch_sprite(id, session)
    await save_sprite(name, sprite, session)


async def fetch_sprite(id, session):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    async with session.get(url) as response:
        data = await response.json()
    return data.get('species').get('name'), data.get('sprites').get('front_default')


async def save_sprite(name, sprite, session):
    async with session.get(sprite) as response:
        content = await response.read()
    if not os.path.exists('pokemons'):
        os.makedirs('pokemons')
    with open(f'pokemons/{name}.png', 'wb') as file:
        file.write(content)


async def test_asyncio():
    async with aiohttp.ClientSession() as session:
        tasks = [generate_pokemon(i, session) for i in range(1, 256)]
        start = time.time()
        await asyncio.gather(*tasks)
        end = time.time()
        duration = end - start
        print(f"With asyncio, execution took {duration} seconds")


if __name__ == "__main__":
    clear_folder()
    asyncio.run(test_asyncio())
