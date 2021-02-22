"""InterSETction
Find the intersection of multiple sets

Usage:
    interset [--input=<input>|-i=<input>] [--method=<method>|-m=<method>] [--output=<output>|-o=<output>]
        [--verbosity|-v|-vv|-vvv] [--log-file=<log_path>]
    interset generate (--output=<output>|-o=<output>) [--sets=<s>|-s=<s>] [--elements=<e>|-e=<e>] [--common=<c>|-c=<c>]
        [--verbosity|-v|-vv|-vvv] [--log-file=<log_file>]
    interset benchmark [--setup] [--verbosity|-v|-vv|-vvv] [--log-file=<log_file>]

Arguments:
    generate    generate the benchmark data (in data folder)
    benchmark   launch the different methods and display results

Options:
    --input=<input> -i=<input>      The file containing the array of sets.
                                    This file should contain one set by line, every entity must be separated by a "\t".
                                    [default: data/input.txt]
    --output=<output> -o=<output>   The file where the resulting set should be stored.
                                    [default: data/output.txt]
    --method=<method> -m=<method>   The method that this script should use to get the intersection
                                    [default: best]
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

from docopt import docopt

from src.benchmark import generate_testing_data
from src.generator.sets import generate
from src.solver.intersection import set_intersection
from src.utils.file import write_sets, load_sets

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
            print('not implemented')

    #
    else:
        method = arguments['--method']
        logging.debug(f'Solving with {method}.')
        sets = load_sets(arguments['--input'])
        m = set_intersection
        a = m(sets)
        print(a)
