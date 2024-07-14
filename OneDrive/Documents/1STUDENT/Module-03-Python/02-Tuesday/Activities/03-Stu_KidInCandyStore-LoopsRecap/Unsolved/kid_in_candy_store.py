# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all the candies selected inside of
candy_cart = []

# Print out options
for i in range(len(candy_list)):
    print(f"[{i}] {candy_list[i]}")

for i in range(allowance):
    select = input("Which candy do you want? ")
    candy_cart.append(candy_list[select])
print(candy_cart)

for candy in candy_cart:
    print(candy)
