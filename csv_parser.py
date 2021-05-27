import csv
from pathlib import Path
import sys


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
            items.append((row[0]))
            # items.append(int(row[0]))
            w.append(float(row[1]))
            v.append(float(row[2]))
            line_count += 1
    return items, w, v


# if len(sys.argv) == 2:
#     data_folder = Path("csv/")
#     csv_path = data_folder / sys.argv[1]
#     items, w, v = getDataFromCsv(csv_path)
#     printDataSet(items, w, v)
#     print("row number: ", len(items))
