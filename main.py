import sys
import time
import os

from pathlib import Path

from csv_parser import getDataFromCsv
from bruteforce import brute_force_solver
from optimized import dynamic_programming_solver


def print_results(cost, best_profit, best_subset, solving_time):
    print("The shares bought:\n")
    best_combination_str = " | ".join("%s" % i for i in best_subset)
    print(best_combination_str, "\n")
    padding = 14
    cost = "€{:.2f}".format(cost)
    best_profit = "€{:.2f}".format(best_profit)
    solving_time = "{:.2f}s".format(solving_time)
    print("Total cost:".ljust(padding), cost, end='\n')
    print("Total return: ".ljust(padding), best_profit)
    print("\nTime solving: ".ljust(padding), solving_time)


if __name__ == '__main__':
    try:
        filename = (sys.argv[1])
    except:
        print('Usage: python main.py FILENAME')
        sys.exit(1)

    path = Path("./")
    csv_path = os.path.join(path, filename)

    # get datas from csv file
    capacity = 500
    items, weights, values = getDataFromCsv(csv_path)
    nb_items = len(items)

    # multiplication by 100 for using integer numbers instead of floats
    capacity *= 100
    for i in range(nb_items):
        weights[i] = int(weights[i] * 100)

    # mutiplication for get the profit values in euro currency instead of percent
    for i in range(nb_items):
        values[i] = weights[i] * values[i]

    # beginning brute force solver
    start = time.time()
    cost, best_profit, best_subset = brute_force_solver(
        nb_items, capacity, weights, values, items)
    stop = time.time()
    solving_time = stop - start
    print_results(cost, best_profit, best_subset, solving_time)

    # beginning dynamic programming solver
    start = time.time()
    cost, best_profit, best_subset = dynamic_programming_solver(
        items, weights, values, capacity, nb_items)
    stop = time.time()
    solving_time = stop - start
    print_results(cost, best_profit, best_subset, solving_time)
