import os
import csv

# Path to collect data from the Resources folder
graduation_csv = os.path.join('..', 'Resources', 'graduation_data.csv')

# Define the function and have it accept the 'state_data' as its sole parameterdef print_percentages(state_data):
    # For readability, it can help to assign your values to variables with descriptive names
    # CSV headers: State or jurisdiction, Adjusted cohort (Public), Completers (Public),
    # Adjusted cohort (Nonprofit Private), Completers (Nonprofit Private),
    # Adjusted cohort (For-profit Private), Completers (For-profit Private)
    state = str(state_data[0])
    public_students = int(state_data[1])
    public_graduates = int(state_data[2])
    nonprofit_students = int(state_data[3])
    nonprofit_graduates = int(state_data[4])
    forprofit_students = int(state_data[5])
    forprofit_graduates = int(state_data[6])

# Find the total students

# Find the total graduates

# Find the public school graduation rate

# Remember that some states do not have nonprofit or forprofit private schools
# Find the non-profit school graduation rate

# Find the for-profit school graduation rate

# Calculate the overall graduation rate

# Print out the state's name and its graduation rates


# Read in the CSV file
with open(graduation_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print_percentages(row)
