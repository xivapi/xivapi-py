import logging
from functools import wraps
from time import time

__log__ = logging.getLogger(__name__)


def timed(func):
    """This decorator prints the execution time for the decorated function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        __log__.info("{} ran in {}s".format(func.__name__, round(end - start, 2)))
        return result
    return wrapper
