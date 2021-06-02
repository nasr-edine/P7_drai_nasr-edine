import sys
import time

from pathlib import Path

from csv_parser import getDataFromCsv, printDataSet
from bruteforce import brute_force

if __name__ == '__main__':
    if len(sys.argv) == 2:
        data_folder = Path("./")
        csv_path = data_folder / sys.argv[1]
        items, w, v = getDataFromCsv(csv_path)
        for i in range(len(v)):
            v[i] = w[i] * v[i] / 100

        n = len(items)
        capacity = 500
    start = time.time()
    cost, best_profit, best_subset = brute_force(
        n, capacity, w, v, items)
    stop = time.time()
    solving_time = stop - start

    print("best cost: ", cost)
    print("best profit: ", best_profit)
    best_combination_str = " ".join("%s" % i for i in best_subset)
    print(best_combination_str)
    # print("numeros actions: ", list_index)
    print("time: ", solving_time)
