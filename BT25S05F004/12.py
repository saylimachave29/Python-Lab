import csv

# File name (make sure this file exists in same folder)
filename = "input.csv"

with open(filename, mode="r", newline="") as file:
    reader = csv.reader(file)

    # If CSV has a header row
    header = next(reader)
    print("Header:", header)

    print("\nData:")
    for row in reader:
        print(row)