import logging

from src.generator.sets import generate
from src.utils.file import write_sets


def generate_testing_data():
    # sets: int, elements: int, common: int
    param = [
        (10, 100, 20),
        (100, 1000, 200),
        (150, 1500, 300),
        (600, 10_000, 500),
        (1000, 1_000_000, 5000),
        (5000, 1_000_000_000, 500_000)
    ]
    for s, e, c in param:
        write_sets(generate(s, e, c), file_path=f'data/set_s{s}_e{e}_c{c}.txt')
    logging.info('The benchmark setup is complete.')
