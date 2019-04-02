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
    XIVAPI Invalid Language error
    """
    pass


class XIVAPIInvalidIndex(Exception):
    """
    XIVAPI Invalid Index error
    """
    pass


class XIVAPIInvalidColumns(Exception):
    """
    XIVAPI Invalid Columns error
    """
    pass


class XIVAPIErrorOrMaintenance(Exception):
    """
    XIVAPI Maintenance error
    """
    pass