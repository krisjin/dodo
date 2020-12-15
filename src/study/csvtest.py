import csv

csv_reader = csv.reader(open('/usr/local/gitrep/dodo/src/resources/testdata.csv', encoding='utf-8'))
for row in csv_reader:
    print(row[0])

