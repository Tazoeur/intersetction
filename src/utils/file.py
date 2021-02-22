from typing import Set, List


def write_sets(sets: List[Set[int]], file_path: str):
    """
    Store the given set in the given file

    :param Set[int] sets: The sets that have to be stored
    :param str file_path: The path where the sets have to be stored
    :return: Nothing
    """
    with open(file_path, 'w') as f:
        f.write('\n'.join(['\t'.join([str(v) for v in s]) for s in sets]))


def load_sets(file_path: str) -> List[Set[int]]:
    """
    Load stored set from disk

    :param str file_path: The path where the file is stored
    :return: The list of sets
    :rtype: List[Set[int]]
    """
    with open(file_path, 'r') as f:
        return [set([int(value) for value in line.split('\t')]) for line in f.read().split('\n')]
