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


class XIVAPIErrorOrMaintenance(Exception):
    """
    XIVAPI maintenance error
    """
    pass