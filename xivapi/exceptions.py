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


class XIVAPIErrorOrMaintenance(Exception):
    """
    XIVAPI Maintenance error
    """
    pass