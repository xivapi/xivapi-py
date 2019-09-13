class XIVAPIForbidden(Exception):
    """
    XIVAPI Forbidden Request error
    """
    pass


class XIVAPIBadRequest(Exception):
    """
    XIVAPI Bad Request error
    """
    pass


class XIVAPINotFound(Exception):
    """
    XIVAPI not found error
    """
    pass


class XIVAPIServiceUnavailable(Exception):
    """
    XIVAPI service unavailable error
    """
    pass


class XIVAPIInvalidLanguage(Exception):
    """
    XIVAPI invalid language error
    """
    pass


class XIVAPIInvalidIndex(Exception):
    """
    XIVAPI invalid index error
    """
    pass


class XIVAPIInvalidColumns(Exception):
    """
    XIVAPI invalid columns error
    """
    pass


class XIVAPIInvalidWorlds(Exception):
    """
    XIVAPI invalid world(s) error
    """
    pass


class XIVAPIInvalidDatacenter(Exception):
    """
    XIVAPI invalid datacenter error
    """
    pass


class XIVAPIError(Exception):
    """
    XIVAPI error
    """
    pass