from functools import reduce
from typing import Set, List, Callable


def methods() -> [(str, Callable)]:
    return [
        ('Set Intersection', set_intersection),
        ('Set Intersection Reduce', set_intersection_reduce),
        ('Binary Reduce', binary_reduce)
    ]


def set_intersection(sets: List[Set[int]]) -> Set[int]:
    return set.intersection(*sets)


def set_intersection_reduce(sets: List[Set[int]]) -> Set[int]:
    return set(reduce(set.intersection, sets))


def binary_reduce(sets: List[Set[int]]) -> Set[int]:
    return set(reduce(lambda s1, s2: s1 & s2, sets))
