# Take input of you and your neighbor
your_first_name = input("What is your name? ")
neighbor_first_name = input("What is your neighbor's first name? ")

# Take how long each of you have been coding
months_you_coded = input("Months I have coded ")
months_neighbor_coded = input("Months neighbor has coded ")

# Add total month
total_months_coded = int(months_you_coded) + int(months_neighbor_coded)
print("I am " + your_first_name + " and my neighbor is " + neighbor_first_name)

# Print results
print("Together we have been coding for " + str(total_months_coded) + " months ")
