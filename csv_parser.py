import csv
from pathlib import Path
import sys

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
        line_count = 0
        for row in csv_reader:
            if float(row[1]) > 0 and float(row[2]) > 0:
                items.append((row[0]))
                w.append(float(row[1]))
                v.append(float(row[2]))
                line_count += 1
    return items, w, v


# data_file_name = sys.argv[1]
# parse input data
# df = pd.read_csv(data_file_name, names=['name', 'price', 'profit'])

# print(df['name'])
# print(df['price'])
# print(list(df['profit']))
# print((df['profit']))
