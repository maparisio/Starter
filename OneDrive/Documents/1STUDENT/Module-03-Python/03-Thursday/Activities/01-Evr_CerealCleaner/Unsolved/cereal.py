import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

# open and read dataset
with open(cereal_csv) as data:
    reader = csv.reader(data, delimiter =",")
    header = next(reader)

    for row in reader:
        fiber = float(row[7])
        if fiber >= 5:
            name = row[0]
            print(name)





