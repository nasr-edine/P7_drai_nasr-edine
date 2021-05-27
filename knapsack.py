import itertools
import sys

from csv_parser import getDataFromCsv, printDataSet
from pathlib import Path

if len(sys.argv) == 2:
    data_folder = Path("csv/")
    csv_path = data_folder / sys.argv[1]
    items, w, v = getDataFromCsv(csv_path)
    # printDataSet(items, w, v)
    # print("row number: ", len(items))
    # exit()

# item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# w = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34,
#      42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
# v = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]

# item = [1, 2, 3]
# w = [20, 30, 50]
# v = [5, 10, 15]

set1 = set(items)
efficiency = 0
total_Value = 0
earnings = 0
max_value = 0

for n in range(1, len(set1) + 1):
    data = itertools.combinations(items, n)
    subsets = set(data)
    # subsets = list(data)
    # exit()
    efficiency += len(subsets)
    for i in subsets:
        total_Value = 0
        earnings = 0
        for j in i:
            # print(j)
            # print(items.index(j)+1)
            # total_Value += w[int(j) - 1]
            total_Value += w[items.index(j)]
            earnings += w[items.index(j)] * v[items.index(j)] / 100
            # earnings += w[int(j) - 1] * v[int(j) - 1] / 100
        if total_Value < 500:
            print("subset: ", i, end=" ")
            print("weight: ", total_Value, end=" ")
            print("earnings: ", earnings)

            if earnings > max_value:
                max_value = earnings
                winner_subset = i
    print("\n")

cost = 0
list_index = []
for i in winner_subset:
    cost += w[items.index(i)]
    list_index.append(items.index(i) + 1)
    # cost += w[i - 1]

print("cout total: ", cost)
print("benefice: ", max_value)
print("actions achetees: ", winner_subset)
print("numeros actions: ", list_index)


efficiency += len(subsets)
print("\nefficiency: " + str(efficiency))
