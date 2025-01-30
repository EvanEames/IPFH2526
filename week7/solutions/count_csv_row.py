import csv
from csv import DictReader
def count_csv_row(csv_file):
    rows = 0
    with open("data.csv", "r") as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            rows+=1
    return rows

print(count_csv_row("data.csv"))