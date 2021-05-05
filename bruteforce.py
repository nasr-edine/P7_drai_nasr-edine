import csv

with open('dataset1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(28 * "-")
            print("|", row[0].ljust(11), end='|')
            print(row[1].ljust(6), end='|')
            print(row[2].ljust(6), end='|\n')
            print(28 * "-")
            line_count += 1
        elif line_count < 5:
            print("|", row[0].ljust(11), end='|')
            print(row[1].ljust(6), end='|')
            print(row[2].ljust(6), end='|\n')
            print(28 * "-")
            line_count += 1
        else:
            break
    print(f'Processed {line_count} lines.')
