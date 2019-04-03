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
import logging

import aiohttp
import xivapi


async def fetch_example_results(session):
    client = xivapi.Client(session=session, api_key="your_key_here")

    # Search Lodestone for a character
    character = await client.character_search(
        world="phoenix", 
        forename="lethys", 
        surname="luculentus"
    )
    print(character)

    # Get a character by Lodestone ID with extended data & include their Free Company information, if it has been synced.
    character = await client.character_by_id(
        id=8255311, 
        extended=True,
        include_freecompany=True
    )
    print(character)

    # Search Lodestone for a free company
    freecompany = await client.freecompany_search(
        world="gilgamesh", 
        name="Elysium"
    )
    print(freecompany)

    # Fuzzy search XIVAPI game data for a recipe by name. Results will be in English.
    recipe = await client.index_search(
        name="Crimson Cider", 
        indexes=["Recipe"], 
        columns=["ID", "Name", "Icon", "ItemResult.Description"], 
        string_algo="fuzzy"
    )
    print(recipe)

    # Fuzzy search XIVAPI game data for a recipe by name. Results will be in French.
    recipe = await client.index_search(
        name="Cidre carmin", 
        indexes=["Recipe"], 
        columns=["ID", "Name", "Icon", "ItemResult.Description"], 
        string_algo="fuzzy", 
        language="fr"
    )
    print(recipe)

    # Get an item by its ID (Omega Rod) and return the data in German
    item = await client.index_by_id(
        index="Item", 
        content_id=23575, 
        columns=["ID", "Name", "Icon", "ItemUICategory.Name"], 
        language="de"
    )
    print(item)

    # Search ingame data for matches against a given query. Includes item, minion, mount & achievement descriptions, quest dialog & more.
    lore = await client.lore_search(
        query="Shiva",
        language="fr"
    )
    print(lore)

    # Get current sales & sale history of an item (Shakshouka) on Phoenix & Odin
    market = await client.market_by_worlds(
        item_id=24280, 
        worlds=["Phoenix", "Odin"]
    )
    print(market)

    # Get current sales & sale history of an item (Shakshouka) on all worlds on the Chaos datacenter with a
    # maximum history of 10
    market = await client.market_by_datacenter(
        item_id=24280, 
        datacenter="Chaos", 
        max_history=10
    )
    print(market)

    await session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')

    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession(loop=loop)
    loop.run_until_complete(fetch_example_results(session))
```
