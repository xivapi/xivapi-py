import asyncio

import aiohttp
import xivapi


async def fetch_example_results(session):
    client = xivapi.Client(session=session, api_key="your_key_here")

    # Search Lodestone for a character
    character = await client.character_search("phoenix", "lethys", "luculentus")
    print(character)

    recipe_columns = ["ID", "Name", "Icon", "ItemResult.Description"]

    # Fuzzy search XIVAPI game data for a recipe by name. Results will be in English.
    recipe = await client.recipe_search("Crimson Cider", columns=recipe_columns, string_algo="fuzzy")
    print(recipe)

    # Fuzzy search XIVAPI game data for a recipe by name. Results will be in French.
    recipe = await client.recipe_search("Cidre carmin", columns=recipe_columns, string_algo="fuzzy", language="fr")
    print(recipe)

    await session.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession(loop=loop)
    loop.run_until_complete(fetch_example_results(session))
