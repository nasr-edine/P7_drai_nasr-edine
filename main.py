import sys
import time
import os

from pathlib import Path

from csv_parser import getDataFromCsv, printDataSet
from bruteforce import brute_force


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

    CAPACITY = 500
    items, weights, values = getDataFromCsv(csv_path)
    nb_items = len(items)

    for i in range(nb_items):
        values[i] = weights[i] * values[i] / 100

    start = time.time()
    cost, best_profit, best_subset = brute_force(
        nb_items, CAPACITY, weights, values, items)
    stop = time.time()
    solving_time = stop - start

    print_results(cost, best_profit, best_subset, solving_time)
