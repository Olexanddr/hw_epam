"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""

import argparse
import math
import operator

def bounded_knapsack(args):
    args.add_argument("-W", type=int, nargs="+")
    args.add_argument("-w", type=str, nargs="+")
    args.add_argument("-n", type=int, nargs="+")
    args_list = args.parse_args()
    bag_weight = args_list.W[0]
    bar_list = args_list.w
    count_bar = args_list.n[0]
    weight_temp = 0
    count = 0
    if str(bag_weight) == "" or bar_list == "" or str(count_bar) == "":
        raise ValueError

    if "." in str(bag_weight) or "." in str(count_bar):
        raise ValueError
    if bag_weight < 0 or count_bar < 0:
        raise ValueError
    for bar in bar_list:
        if "." in bar:
            raise ValueError
        if "-" in bar:
            raise ValueError


    if len(bar_list) > count_bar:
        raise ValueError

    bar_list_int = []
    for bar in bar_list:
        bar_list_int.append(int(bar))
    count_bar = int(count_bar)
    bag_weight = int(bag_weight)
    while weight_temp < bag_weight and count < count_bar and len(bar_list_int) != 0:
        weight_temp += max(bar_list_int)
        count+=1
        bar_list_int.remove(max(bar_list_int))
    return weight_temp

def main():
    args = argparse.ArgumentParser()
    print(bounded_knapsack(args))


if __name__ == '__main__':
    main()
