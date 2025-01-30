import csv
from csv import DictReader

def calculate_column_average(csv_file, column_name):
    total = 0
    count = 0
    with open(csv_file, "r") as my_csv:
        data = DictReader(my_csv)
        for row in data:
            total += int(row[column_name])
            count+=1
    return total/count

print(calculate_column_average("data.csv", "age"))