# xivapi.py
An asynchronous Python client for XIVAPI

## Requirements
```
asyncio
aiohttp
```

## Installation
```
pip install xivapi.py
```

## Example
```python
import asyncio

import aiohttp
import xivapi


async def fetch_example_results(session):
    client = xivapi.Client(session=session, api_key="your_key_here")

    # Search Lodestone for a character
    character = await client.character_search("phoenix", "lethys", "luculentus")
    print(character)

    # Fuzzy search XIVAPI game data for a recipe by name. Results will be in English.
    recipe = await client.index_search("Crimson Cider", 
        indexes=["Recipe"], 
        columns=["ID", "Name", "Icon", "ItemResult.Description"], 
        string_algo="fuzzy")
    print(recipe)

    # Fuzzy search XIVAPI game data for a recipe by name. Results will be in French.
    recipe = await client.index_search("Cidre carmin", 
        indexes=["Recipe"], 
        columns=["ID", "Name", "Icon", "ItemResult.Description"], 
        string_algo="fuzzy", 
        language="fr")
    print(recipe)

    # Get an item by its ID (Omega Rod) and return the data in German
    item = await client.index_by_id(index="Item", 
        content_id=23575, 
        columns=["ID", "Name", "Icon", "ItemUICategory.Name"], 
        language="de")
    print(item)

    await session.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession(loop=loop)
    loop.run_until_complete(fetch_example_results(session))
```
