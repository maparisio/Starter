# @TODO: Your cmy_info = {"name": "Michael",
my_info = {"name": "Michael",
           "occupation": "student",
           "age": 29,
           "hobbies": ["hiking", "sports", "sleeping", "movies"],
           "wake-up": {"Mon": 5, "Friday": 5, "Saturday": 10, "Sunday": 9}}

# Print out results are stored in the dictionary
print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f'On the weekend I get up at {my_info["wake-up"]["Saturday"]}')
