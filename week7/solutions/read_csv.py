import csv
from csv import DictReader
def read_csv(filename):
    with open(filename, "r") as csvfile:
        reader = DictReader(csvfile)
    return reader

print(read_csv("data.csv"))

