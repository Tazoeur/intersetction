import logging
from random import randint
from typing import List, Set


def fill_set(n: int, low: int, high: int, forbidden: Set[int] = None) -> Set[int]:
    """
    Fill a set with `n` values from `low` to `high` that are not in `forbidden`.

    :param int n: The number of element in the set.
    :param int low: The lowest value that can be in the set.
    :param int high: The highest value that can be in the set.
    :param Set[int] forbidden: A set of forbidden values.
    :return: A set.
    :rtype Set[int]:
    """
    if forbidden is None:
        forbidden = set()
    s = set()
    while len(s) < n:
        v = randint(low, high)
        if v not in forbidden:
            s.add(v)
    return s


def generate(sets: int, elements: int, common: int) -> List[Set[int]]:
    """
    Generate a list of set of integer.

    :param int sets: The number of sets that has to be generated.
    :param int elements: The number of elements in each set.
    :param int common: The number of common elements through all sets.
    :return: The array of all sets generated.
    :rtype List[Set[int]]:
    """
    logging.debug(f'Generating {sets} sets with {elements} elements ({common} in common).')
    threshold = 100 * elements
    tab_common = fill_set(common, 1, threshold)
    tab_sets = []
    for _i in range(sets):
        tab_sets.append(set.union(tab_common, fill_set(elements - common, 1, threshold, tab_common)))
    logging.debug('Sets generated.')
    return tab_sets
