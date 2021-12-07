""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Number = Digit{Digit}
Sign = '+' | '-'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = '-123' result = (False, None)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""

import argparse

def check_formula(args):
    args.add_argument("user_input", type=str, nargs="+")
    args_list = args.parse_args()
    expression  = args_list.user_input[0]
    if len(expression) == 0:
        return(False, None)
    if expression[0] in "+-":
        return(False, None)
    if len(args_list.user_input) > 1 or  "++" in expression or "--" in expression or (not expression.replace("+", "").replace("-","").isdigit()) or len(expression) == 0:
        return(False, None)
    else:
        return(True, eval(expression))


def main():
    args = argparse.ArgumentParser()  # Hint: use methods from argparse module
    print(check_formula(args))


if __name__ == '__main__':
    main()
