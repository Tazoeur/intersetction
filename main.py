"""InterSETction
Find the intersection of multiple sets

Usage:
    interset generate (--output=<output>|-o=<output>) [--sets=<s>|-s=<s>] [--elements=<e>|-e=<e>] [--common=<c>|-c=<c>]
        [--verbosity|-v|-vv|-vvv] [--log-file=<log_file>]
    interset benchmark [--setup] [--verbosity|-v|-vv|-vvv] [--log-file=<log_file>]
    interset list (methods|datasets) [--verbosity|-v|-vv|-vvv] [--log-file=<log_file>]

Arguments:
    generate    generate the benchmark data (in data folder).
    benchmark   launch the different methods and display results.
    list        list the available methods or datasets.

Options:
    --input=<input> -i=<input>      The file containing the array of sets.
                                    This file should contain one set by line, every entity must be separated by a "\t".
                                    [default: data/input.txt]
    --output=<output> -o=<output>   The file where the resulting set should be stored.
                                    [default: data/output.txt]
    --sets=<s> -s=<s>               The number of sets. [default: 10]
    --elements=<e> -e=<e>           The number of elements in each set. [default: 100]
    --common=<c> -c=<c>             The number of common elements in each set.
                                    Of course this should be less or equal than the number of elements. [default: 20]
    --setup                         Generate a lot of files to benchmark
    --verbosity -v                  The level of verbosity.
    --log-file=<log-file>           The file where the log should be stored (if any).
    --version -V                    Display the version of this script.
    --help -h                       Display this screen.
"""
import logging
import os

from docopt import docopt

from src.benchmark import generate_testing_data, data, get_data_file_name, measure_solving_time, display_results
from src.generator.sets import generate
from src.solver.intersection import methods
from src.utils.file import write_sets

if __name__ == '__main__':
    arguments = docopt(__doc__, version='InterSETction 0.1')

    # set log level
    if arguments['--verbosity'] > 2:
        log_lvl = logging.DEBUG
    elif arguments['--verbosity'] == 2:
        log_lvl = logging.INFO
    elif arguments['--verbosity'] == 1:
        log_lvl = logging.WARNING
    else:
        log_lvl = logging.ERROR

    # check if there is a log file
    log_file = arguments['--log-file']

    # configure logger
    logging.basicConfig(filename=log_file, level=log_lvl, format='%(levelname)s: %(message)s')
    logging.debug('Begin script')

    # launch script
    # generate an array of set
    if arguments['generate']:
        logging.debug('Generate subcommand selected.')
        sets = generate(int(arguments['--sets']), int(arguments['--elements']), int(arguments['--common']))
        write_sets(sets, arguments['--output'])
        logging.info(f'Sets generated and stored to file {arguments["--output"]}.')

    # Benchmark
    elif arguments['benchmark']:
        logging.debug('Benchmark subcommand selected.')
        # Generate for the benchmark
        if arguments['--setup']:
            generate_testing_data()

        # Launch the actual benchmark
        else:
            results = measure_solving_time(
                [(f'{s}sets%{e}elements%{c}commons', os.path.abspath(get_data_file_name(s, e, c))) for s, e, c in data],
                methods())
            display_results(results)

    # List
    elif arguments['list']:
        if arguments['methods']:
            print('The following methods are implemented for benchmark testing :')
            for m, _f in methods():
                print(f'\t- {m}')
        elif arguments['datasets']:
            print('The following datasets are available for benchmark testing :')
            for file in os.listdir('data'):
                if not file.endswith('.txt'):
                    continue
                else:
                    print(f'\t- {file}')
