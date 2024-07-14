import csv
import os

# Three Lists
indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

# Zip all three lists together into tuples
roster = zip(indexes, employees, department)

# (1, 'Michael', 'Boss')
# (2, 'Dwight', 'Sales')
# (3, 'Meredith', 'Sales')
# (4, 'Kelly', 'HR')

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Index", "Employee", "Department"])
    for employee in roster:
        writer.writerow(employee)


# # to print out to terminal:
# #comment out above code and run the code below
# for employee in roster:
#     print(employee)
