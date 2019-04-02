import asyncio
import logging

import aiohttp

from .exceptions import XIVAPIBadRequest, XIVAPIForbidden, XIVAPIInvalidLanguage, XIVAPIErrorOrMaintenance

__log__ = logging.getLogger(__name__)


class Client:
    """
    Client for accessing XIVAPI's endpoints.

    :ivar api_key: The API key used for identifying your application with XIVAPI.com.
    """

    def __init__(self, session, api_key):
        self.session = session
        self.api_key = api_key

        self.base_url = "https://xivapi.com"
        self.languages = ["en", "fr", "de", "ja"]


    async def character_search(self, world, forename, surname):
        """|coro|
        Search for character data directly from the Lodestone.
        Parameters
        ------------
        world: str
            The world that the character is attributed to.
        forename: str
            The character's forename.
        surname: str
            The character's surname.
        """
        url = f'{self.base_url}/character/search?name={forename}%20{surname}&server={world}&private_key={self.api_key}'
        async with self.session.get(url) as response:
            return await self.process_response(response)


    async def character_by_id(self, lodestone_id):
        """|coro|
        Request character data from XIVAPI.com
        Parameters
        ------------
        lodestone_id: str
            The character's Lodestone ID.
        """
        url = f'{self.base_url}/character/{lodestone_id}?private_key={self.api_key}'
        async with self.session.get(url) as response:
            return await self.process_response(response)
    

    async def freecompany_search(self, world, name):
        """|coro|
        Search for Free Company data directly from the Lodestone.
        Parameters
        ------------
        world: str
            The world that the Free Company is attributed to.
        name: str
            The Free Company's name.
        """
        url = f'{self.base_url}/freecompany/search?name={name}&server={world}&private_key={self.api_key}'
        async with self.session.get(url) as response:
            return await self.process_response(response)


    async def freecompany_by_id(self, lodestone_id):
        """|coro|
        Request Free Company data from XIVAPI.com by Lodestone ID
        Parameters
        ------------
        lodestone_id: str
            The Free Company's Lodestone ID.
        """
        url = f'{self.base_url}/freecompany/{lodestone_id}?private_key={self.api_key}'
        async with self.session.get(url) as response:
            return await self.process_response(response)
    

    async def recipe_search(self, name, columns=[], string_algo=None, language="en"):
        """|coro|
        Search for rceipe data.
        Parameters
        ------------
        name: str
            The name of the item to retrieve the recipe data for.
        Optional[columns: list]
            A named list of columns to return in the response. ID, Name, Icon & ItemDescription will be returned by default.
            e.g. ["ID", "Name", "Icon", "ItemResult.Description"]
        Optional[string_algo: str]
            The string algorithm to use for matching results. Defaults to wildcard if None.
        Optional[language: str]
            The two character length language code that indicates the language to return the response in. Defaults to English (en).
            Valid values are "en", "fr", "de" & "ja"
        """

        if language.lower() not in self.languages:
            raise XIVAPIInvalidLanguage(f'"{language}" is not a valid language code for XIVAPI.')

        params = {
            "indexes": "Recipe",
            "private_key": self.api_key,
            "language": language
        }

        if len(columns) > 0:
            params["columns"] = ",".join(list(set(columns)))

        if string_algo:
            params["string_algo"] = string_algo

        url = f'{self.base_url}/search?string={name}'
        async with self.session.get(url, params=params) as response:
            return await self.process_response(response)


    async def process_response(self, response):
        __log__.info(f'{response.status} from {response.url}')

        if response.status == 200:
            return await response.json()

        if response.status == 401:
            raise XIVAPIForbidden("Request was refused. Possibly due to an invalid API key.")

        if response.status == 500:
            raise XIVAPIErrorOrMaintenance("An internal server error has occured on XIVAPI. This could be due to the Lodestone undergoing maintenance.")

