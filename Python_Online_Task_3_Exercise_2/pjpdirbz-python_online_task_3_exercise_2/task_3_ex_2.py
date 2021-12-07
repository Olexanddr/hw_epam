"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""

import argparse
def from_roman_numerals(args):
    args.add_argument("n", type=str, nargs="+")
    args_list = args.parse_args()
    result = 0
    rome_number = args_list.n[0]
    rome_number_dict = {"I": 1,
                        "IV":4,
                        "V": 5,
                        "IX":9,
                        "X":10,
                        "L":50,
                        "C": 100}
    for i in rome_number:
        if i not in rome_number_dict.keys():
            raise ValueError
    end_index = len(rome_number)
    if len(rome_number) >=2 and rome_number[-2]+rome_number[-1] == "IV":
        result+=4
        end_index-=2
    elif len(rome_number) >=2 and rome_number[-2]+rome_number[-1] == "IX":
        result +=9
        end_index-=2
    for i in range(end_index):
        result+=rome_number_dict[rome_number[i]]
    return result


def main():
    args = argparse.ArgumentParser()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
