import logging
import time
from os import PathLike
from typing import Callable, Dict

from src.generator.sets import generate
from src.utils.file import write_sets, load_sets

# sets: int, elements: int, common: int
data = [
    (10, 100, 20),
    (100, 1000, 200),
    (150, 1500, 300),
    (600, 10_000, 500),
    (1000, 50_000, 5000),
    (1500, 50_000, 5000)
]


def get_data_file_name(s: int, e: int, c: int) -> str:
    """
    Get the name of the data storage file from the parameter of the dataset.

    :param s: The number of sets.
    :param e: The number of elements in each set.
    :param c: The number of common elements in each set.
    :return: The name of the storage file. Please note that this file may not exist.
    :rtype: str
    """
    return f'data/set_s{s}_e{e}_c{c}.txt'


def generate_testing_data():
    """
    Generate storage file containing enough data to be exploitable by benchmark.
    """
    global data

    for s, e, c in data:
        write_sets(generate(s, e, c), file_path=get_data_file_name(s, e, c))
    logging.info('The benchmark setup is complete.')


def measure_solving_time(datasets: [(str, PathLike)], methods: [(str, Callable)]) -> Dict[str, Dict[str, float]]:
    tab = {}
    for dataset_name, dataset in datasets:
        tab[dataset_name] = {}
        for method_name, method in methods:
            sets = load_sets(dataset)
            ping = time.time()
            _solution = method(sets)
            pong = time.time()
            elapsed = pong - ping
            logging.info(f'The method {method_name} took {elapsed}s to complete dataset {dataset_name}.')
            tab[dataset_name][method_name] = elapsed
    return tab


def display_results(results: Dict[str, Dict[str, float]]):
    datasets = list(set([d for d in results]))
    header = ' '.join([f'{m:<25}' for m in results[datasets[0]]])
    print(f"{'dataset':<40} {header}")
    for d in datasets:
        line = ' '.join([f'{results[d][m]:<25}' for m in results[d]])
        print(f'{d:<40} {line}')
