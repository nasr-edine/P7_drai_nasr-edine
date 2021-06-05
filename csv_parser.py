import csv


def getDataFromCsv(dataFile):
    items = []
    weights = []
    values = []
    with open(dataFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if float(row[1]) > 0 and float(row[2]) > 0:
                items.append((row[0]))
                weights.append(float(row[1]))
                values.append(float(row[2]))
    return items, weights, values
