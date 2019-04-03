import asyncio
import logging

import aiohttp

from .exceptions import XIVAPIBadRequest, XIVAPIForbidden, XIVAPIInvalidLanguage, XIVAPIErrorOrMaintenance, XIVAPIInvalidIndex, XIVAPIInvalidColumns, XIVAPIInvalidWorlds, XIVAPIInvalidDatacenter

__log__ = logging.getLogger(__name__)


class Client:
    """
    Asynchronous client for accessing XIVAPI's endpoints.
    Parameters
    ------------
    session: aiohttp.ClientSession()
        The aiohttp session used with which to make http requests
    api_key: str
        The API key used for identifying your application with XIVAPI.com.
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


    async def character_by_id(self, lodestone_id: int, extended=False, include_achievements=False, include_freecompany=False, include_freecompany_members=False, include_pvpteam=False):
        """|coro|
        Request character data from XIVAPI.com
        Please see XIVAPI documentation for more information about character sync state https://xivapi.com/docs/Character#character
        Parameters
        ------------
        lodestone_id: int
            The character's Lodestone ID.
        """

        params = {
            "private_key": self.api_key
        }

        if extended is True:
            params["extended"] = 1

        data = []
        if include_achievements is True:
            data.append("AC")

        if include_freecompany is True:
            data.append("FC")

        if include_freecompany_members is True:
            data.append("FCM")

        if include_pvpteam is True:
            data.append("PVP")

        if len(data) > 0:
            params["data"] = ",".join(data)

        url = f'{self.base_url}/character/{lodestone_id}'
        async with self.session.get(url) as response:
            return await self.process_response(response)


    async def character_verify(self, lodestone_id: int, token):
        """|coro|
        Request character data from XIVAPI.com
        Parameters
        ------------
        lodestone_id: int
            The character's Lodestone ID.
        token: str
            The string token on a character's Lodestone profile to test against
        """

        params = {
            "private_key": self.api_key,
            "token": token
        }

        url = f'{self.base_url}/character/{lodestone_id}/verification'
        async with self.session.get(url, params=params) as response:
            return await self.process_response(response)


    async def character_update(self, lodestone_id: int):
        """|coro|
        Request a character to be updated as soon as possible
        Parameters
        ------------
        lodestone_id: int
            The character's Lodestone ID.
        """
        url = f'{self.base_url}/character/{lodestone_id}/update?private_key={self.api_key}'
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


    async def freecompany_by_id(self, lodestone_id: int):
        """|coro|
        Request Free Company data from XIVAPI.com by Lodestone ID
        Parameters
        ------------
        lodestone_id: int
            The Free Company's Lodestone ID.
        """
        url = f'{self.base_url}/freecompany/{lodestone_id}?private_key={self.api_key}'
        async with self.session.get(url) as response:
            return await self.process_response(response)


    async def linkshell_search(self, world, name):
        """|coro|
        Search for Linkshell data directly from the Lodestone.
        Parameters
        ------------
        world: str
            The world that the Linkshell is attributed to.
        name: str
            The Linkshell's name.
        """
        url = f'{self.base_url}/linkshell/search?name={name}&server={world}&private_key={self.api_key}'
        async with self.session.get(url) as response:
            return await self.process_response(response)


    async def linkshell_by_id(self, lodestone_id: int):
        """|coro|
        Request Linkshell data from XIVAPI.com by Lodestone ID
        Parameters
        ------------
        lodestone_id: int
            The Linkshell's Lodestone ID.
        """
        url = f'{self.base_url}/linkshell/{lodestone_id}?private_key={self.api_key}'
        async with self.session.get(url) as response:
            return await self.process_response(response)


    async def pvpteam_search(self, world, name):
        """|coro|
        Search for PvPTeam data directly from the Lodestone.
        Parameters
        ------------
        world: str
            The world that the PvPTeam is attributed to.
        name: str
            The PvPTeam's name.
        """
        url = f'{self.base_url}/pvpteam/search?name={name}&server={world}&private_key={self.api_key}'
        async with self.session.get(url) as response:
            return await self.process_response(response)


    async def pvpteam_by_id(self, lodestone_id: int):
        """|coro|
        Request PvPTeam data from XIVAPI.com by Lodestone ID
        Parameters
        ------------
        lodestone_id: int
            The PvPTeam's Lodestone ID.
        """
        url = f'{self.base_url}/pvpteam/{lodestone_id}?private_key={self.api_key}'
        async with self.session.get(url) as response:
            return await self.process_response(response)
    

    async def index_search(self, name, indexes=[], columns=[], string_algo=None, language="en"):
        """|coro|
        Search for data from on specific indexes.
        Parameters
        ------------
        name: str
            The name of the item to retrieve the recipe data for.
        indexes: list
            A named list of indexes to search XIVAPI. At least one must be specified.
            e.g. ["Recipe", "Item"]
        Optional[columns: list]
            A named list of columns to return in the response. ID, Name, Icon & ItemDescription will be returned by default.
            e.g. ["ID", "Name", "Icon"]
        Optional[string_algo: str]
            The string algorithm to use for matching results. Defaults to wildcard if None.
        Optional[language: str]
            The two character length language code that indicates the language to return the response in. Defaults to English (en).
            Valid values are "en", "fr", "de" & "ja"
        """

        if len(indexes) == 0:
            raise XIVAPIInvalidIndex("Please specify at least one index to search for, e.g. [\"Recipe\"]")

        if language.lower() not in self.languages:
            raise XIVAPIInvalidLanguage(f'"{language}" is not a valid language code for XIVAPI.')

        if len(columns) == 0:
            raise XIVAPIInvalidColumns("Please specify at least one column to return in the resulting data.")

        params = {
            "private_key": self.api_key,
            "language": language,
            "indexes": ",".join(list(set(indexes))),
            "string": name
        }

        if len(columns) > 0:
            params["columns"] = ",".join(list(set(columns)))

        if string_algo:
            params["string_algo"] = string_algo

        url = f'{self.base_url}/search'
        async with self.session.get(url, params=params) as response:
            return await self.process_response(response)


    async def index_by_id(self, index, content_id: int, columns=[], language="en"):
        """|coro|
        Request data from a given index by ID.
        Parameters
        ------------
        index: str
            The index to which the content is attributed.
        content_id: int
            The ID of the content
        Optional[columns: list]
            A named list of columns to return in the response. ID, Name, Icon & ItemDescription will be returned by default.
            e.g. ["ID", "Name", "Icon"]
        Optional[language: str]
            The two character length language code that indicates the language to return the response in. Defaults to English (en).
            Valid values are "en", "fr", "de" & "ja"
        """
        if index == "":
            raise XIVAPIInvalidIndex("Please specify an index to search on, e.g. \"Item\"")

        if len(columns) == 0:
            raise XIVAPIInvalidColumns("Please specify at least one column to return in the resulting data.")

        params = {
            "private_key": self.api_key,
            "language": language
        }

        if len(columns) > 0:
            params["columns"] = ",".join(list(set(columns)))

        url = f'{self.base_url}/{index}/{content_id}'
        async with self.session.get(url, params=params) as response:
            return await self.process_response(response)


    async def lore_search(self, query, language="en"):
        """|coro|
        Search cutscene subtitles, quest dialog, item, achievement, mount & minion descriptions and more for any text that matches query.
        Parameters
        ------------
        query: str
            The text to search game content for.
        Optional[language: str]
            The two character length language code that indicates the language to return the response in. Defaults to English (en).
            Valid values are "en", "fr", "de" & "ja"
        """
        params = {
            "private_key": self.api_key,
            "language": language,
            "string": query
        }

        url = f'{self.base_url}/lore'
        async with self.session.get(url, params=params) as response:
            return await self.process_response(response)


    async def market_by_worlds(self, item_id: int, worlds=[], max_history=25):
        """|coro|
        Request current sale listings & sale history for a given item on specified FFXIV worlds.
        Parameters
        ------------
        item_id: int
            The ID of the sellable item.
        worlds: list
            A named list of worlds to return in the response. At least one world is required.
            e.g. ["Phoenix", "Gilgamesh", "Tonberry"]
        Optional[max_history: int]
            The maximum number of history records to return. Default is 25.
        """
        worlds_count = len(worlds)
        if worlds_count < 1 or worlds_count > 15:
             raise XIVAPIInvalidWorlds("Please provide a list of valid names of FFXIV worlds e.g. [\"Phoenix\", \"Gilgamesh\", \"Tonberry\"]")

        params = {
            "private_key": self.api_key,
            "servers": ",".join(list(set(worlds))),
            "max_history": max_history
        }

        url = f'{self.base_url}/market/item/{item_id}'
        async with self.session.get(url, params=params) as response:
            return await self.process_response(response)


    async def market_by_datacenter(self, item_id: int, datacenter, max_history=25):
        """|coro|
        Request current sale listings & sale history for a given item on all worlds on a specified FFXIV datacenter.
        Parameters
        ------------
        item_id: int
            The ID of the sellable item.
        datacenter: str
            The name of the FFXIV datacenter from which to request data.
        Optional[max_history: int]
            The maximum number of history records to return. Default is 25.
        """
        if datacenter == "":
            raise XIVAPIInvalidDatacenter("Please provide a valid name of an FFXIV Datacenter e.g. \"Chaos\", \"Aether\", \"Elemental\", e.t.c.")

        params = {
            "private_key": self.api_key,
            "dc": datacenter,
            "max_history": max_history
        }

        url = f'{self.base_url}/market/item/{item_id}'
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

