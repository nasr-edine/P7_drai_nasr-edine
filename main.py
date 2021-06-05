import time
import argparse

from csv_parser import getDataFromCsv
from bruteforce import brute_force_solver
from optimized import dynamic_programming_solver

BRUTE_FORCE = "brute"
DYNAMIC_PROGRAMMING = "dynamic"


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

    parser = argparse.ArgumentParser(
        description='Script solving the best shares to buy for 500€ problem')
    parser.add_argument('-f', required=True, type=str, dest="filename",
                        help='Path to csv file')
    parser.add_argument("-m", default=BRUTE_FORCE, type=str, dest="method",
                        choices=[BRUTE_FORCE, DYNAMIC_PROGRAMMING],
                        help="Solving method. "
                        "Default value: brute force method")
    args = parser.parse_args()

    csv_path = args.filename

    # get datas from csv file
    items, weights, values = getDataFromCsv(csv_path)
    nb_items = len(items)
    capacity = 500

    # multiplication by 100 for using integer numbers instead of floats
    capacity *= 100
    for i in range(nb_items):
        weights[i] = int(weights[i] * 100)

    # mutiplication for get the profit values in euro currency
    for i in range(nb_items):
        values[i] = weights[i] * values[i]

    start = time.time()
    # selecting problem solving algorithm
    if args.method == BRUTE_FORCE:
        cost, best_profit, best_subset = brute_force_solver(
            nb_items, capacity, weights, values, items)
    if args.method == DYNAMIC_PROGRAMMING:
        cost, best_profit, best_subset = dynamic_programming_solver(
            items, weights, values, capacity, nb_items)

    stop = time.time()
    solving_time = stop - start
    print_results(cost, best_profit, best_subset, solving_time)
