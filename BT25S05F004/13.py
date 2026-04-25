import csv

# Data to write into CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 21, "Pune"],
    ["Bob", 22, "Mumbai"],
    ["Charlie", 23, "Delhi"]
]

# Open a CSV file in write mode
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write multiple rows
    writer.writerows(data)

print("CSV file written successfully!")