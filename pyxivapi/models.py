from .exceptions import XIVAPIInvalidFilter

class Filter:
    """
    Model class for DQL filters
    """

    comparisons = ["gt", "gte", "lt", "lte"]

    def __init__(self, field: str, comparison: str, value: int):
        comparison = comparison.lower()

        if comparison not in self.comparisons:
            raise XIVAPIInvalidFilter(f'"{comparison}" is not a valid DQL filter comparison.')

        self.Field = field
        self.Comparison = comparison
        self.Value = value


class Sort:
    """
    Model class for sort field
    """

    def __init__(self, field: str, ascending: bool):
        self.Field = field
        self.Ascending = ascending
