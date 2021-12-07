"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import math
import operator

def calculate(args):
    args.add_argument("arg1", type=str, nargs="+")
    args_list = args.parse_args()
    function_name = args_list.arg1[0]
    arg_1 = args_list.arg1[1]
    if not bool(getattr(math, function_name, False) or getattr(operator, function_name, False)):
        raise NotImplementedError
    if len(args_list.arg1) == 3 and bool(getattr(math, function_name, False)):
        arg_2 = args_list.arg1[2]
        if (function_name == "truediv" or function_name == "floor div" or function_name == "mod") and float(arg_2) == 0:
            raise NotImplementedError
        return getattr(math, function_name)(float(arg_1),float(arg_2))
    elif len(args_list.arg1) == 3 and bool(getattr(operator, function_name, False)):
        arg_2 = args_list.arg1[2]
        if (function_name == "truediv" or function_name == "floor div" or function_name == "mod") and float(arg_2) == 0:
            raise NotImplementedError
        return getattr(operator, function_name)(float(arg_1),float(arg_2))
    elif len(args_list.arg1) == 2 and bool(getattr(math, function_name, False)):
        return getattr(math, function_name)(float(arg_1))
    elif len(args_list.arg1) == 2 and bool(getattr(operator, function_name, False)):
        return getattr(math, function_name)(float(arg_1))
    else:
        raise NotImplementedError


def main():
    args = argparse.ArgumentParser()
    print(calculate(args))


if __name__ == '__main__':
    main()
