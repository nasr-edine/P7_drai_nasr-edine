import itertools
import sys
import time
from csv_parser import getDataFromCsv, printDataSet
from pathlib import Path


# print(v)
# input()
# item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# w = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34,
#      42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
# v = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]

# item = [1, 2, 3]
# w = [20, 30, 50]
# v = [5, 10, 15]


def brute_force(n, capacity, w, v, items):
    """Brute force method for solving knapsack problem
    :param n: number of existing items
    :param capacity: the capacity of knapsack
    :param w: list of weights
    :param v: list of values
    :return: tuple like: (best cost, best combination list(contains 1 and 0))
    """
    # set1 = set(items)
    # print(len(set1))
    # print(n)
    # input()
    # efficiency = 0
    total_Value = 0
    earnings = 0
    max_value = 0
    start = time.time()

    for index in range(n):
        # print("index: ", index)
        # input()
        data = itertools.combinations(items, index + 1)
        # print("data: ", set(data))
        # input()
        subsets = set(data)
        # efficiency += len(subsets)
        for i in subsets:
            total_Value = 0
            earnings = 0
            for j in i:
                total_Value += w[items.index(j)]
                earnings += v[items.index(j)]
            if total_Value <= capacity:
                if earnings > max_value:
                    max_value = earnings
                    winner_subset = i
    cost = 0
    list_index = []
    for i in winner_subset:
        cost += w[items.index(i)]
        list_index.append(items.index(i) + 1)
    stop = time.time()
    duree = stop - start
    print("cout total: ", cost)
    print("benefice: ", max_value)
    print("actions achetees: ", winner_subset)
    print("numeros actions: ", list_index)
    print("time: ", duree)


if len(sys.argv) == 2:
    data_folder = Path("csv/")
    csv_path = data_folder / sys.argv[1]
    items, w, v = getDataFromCsv(csv_path)
    # printDataSet(items, w, v)
    # print("row number: ", len(items))
    # exit()
    for i in range(len(v)):
        v[i] = w[i] * v[i] / 100
    n = len(items)
    capacity = 500
brute_force(n, capacity, w, v, items)
