"""Task 1
For a given integer n calculate the value which is equal to a:
- squared number, if its value is strictly positive;
- modulus of a number, if its value is strictly negative;
- zero, if the integer n is zero.

Example,
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64
"""
import argparse

def calculate(args):
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
    print(calculate(args))


if __name__ == '__main__':
    main()
