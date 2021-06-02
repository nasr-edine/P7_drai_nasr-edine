import itertools
import sys

from csv_parser import getDataFromCsv, printDataSet
from pathlib import Path

if len(sys.argv) == 2:
    data_folder = Path("csv/")
    csv_path = data_folder / sys.argv[1]
    items, w, v = getDataFromCsv(csv_path)

# | Item | Weight | Value |
# |------|--------|-------|
# | 1    | 2      | 1     |
# | 2    | 10     | 20    |
# | 3    | 3      | 3     |
# | 4    | 6      | 14    |
# | 5    | 18     | 100   |

# Put a placeholder 0 weight, 0 value item to max
# these line up better with the 1D memoization table K
# item_weights = [0, 2, 10, 3, 6, 18]
# item_values = [0, 1, 20, 3, 14, 100]

# item_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# item_weights = [20, 30, 50, 70, 60, 80, 22, 26,
#                 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
# item_values = [5, 10, 15, 20, 17, 25, 7, 11,
#                13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
item_weights = w
item_values = v

for i in range(len(item_weights)):
    value = item_weights[i] * item_values[i] / 100
    print(value, end=' ')
    item_values[i] = value
n = len(item_weights)
W = 500  # total weight capacity
K = [[0 for w in range(W + 1)] for i in range(n)]

# Recurrence
for i in range(1, n):
    for w in range(1, W + 1):
        wi = item_weights[i]
        vi = item_values[i]

        if wi <= w:
            print(i)
            print(w)
            print(wi)
            K[i][w] = max([K[i - 1][w - wi] + vi, K[i - 1][w]])
        else:
            K[i][w] = K[i - 1][w]

# Results
print("Result: ", K[n - 1][W])

# Optional: Uncomment to view the 2D table
# from pandas import *
# print("K table:")
# print(DataFrame(K))
