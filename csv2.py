import csv
filename = 'records.csv'
fields = []
rows = []

with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    print(dialect)
    csv_f.seek(0)

    csvreader = csv.reader(csv_f, delimiter=":")

    print(csvreader)

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(fields)
print(rows)
