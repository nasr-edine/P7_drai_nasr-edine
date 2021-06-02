import csv
from pathlib import Path
import sys
import collections

# import pandas as pd


def printDataSet(items, w, v):
    print(19 * "-")
    for i in range(len(items)):
        print("|", str(items[i]).ljust(4), end='|')
        print(str(w[i]).ljust(5), end='|')
        print(str(v[i]).ljust(5), end='|\n')
        print(19 * "-")


def getDataFromCsv(dataFile):
    items = []
    w = []
    v = []
    with open(dataFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if float(row[1]) > 0 and float(row[2]) > 0:
                items.append((row[0]))
                w.append(float(row[1]))
                v.append(float(row[2]))

    duplicate_shares = [item for item,
                        count in collections.Counter(items).items() if count > 1]
    indices = []
    for j in range(len(duplicate_shares)):
        res = ([i for i, x in enumerate(items) if x == duplicate_shares[j]])
        indices += res

    for indice in indices:
        items.pop(indice)
        w.pop(indice)
        v.pop(indice)
    return items, w, v
