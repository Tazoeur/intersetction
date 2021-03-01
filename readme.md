# InterSETction

## Requirements

`docopt` is the only requirement.

You can install it either by running `pip install docopt` or by running `pip install -r requirements.txt`.

## Usage

You can find the following documentation with the `--help` option.

```
InterSETction

Find the intersection of multiple sets.

Usage:
    interset [--input=<input>|-i=<input>] [--method=<method>|-m=<method>] [--output=<output>|-o=<output>]
        [--verbosity|-v|-vv|-vvv] [--log-file=<log_path>]
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
```

## Results

```
dataset                                  Set Intersection          Set Intersection Reduce   Binary Reduce            
10sets%100elements%20commons             2.5033950805664062e-05    2.6702880859375e-05       2.002716064453125e-05    
100sets%1000elements%200commons          0.0008323192596435547     0.000896453857421875      0.0010635852813720703    
150sets%1500elements%300commons          0.004316091537475586      0.0043392181396484375     0.0045013427734375       
600sets%10000elements%500commons         0.048795461654663086      0.04901933670043945       0.05125308036804199      
1000sets%50000elements%5000commons       0.690288782119751         0.7071182727813721        0.6256792545318604       
1500sets%50000elements%5000commons       1.0401890277862549        0.9484059810638428        1.0698180198669434       
```