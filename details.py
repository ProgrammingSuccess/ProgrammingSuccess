# Get the following information from the user, with an input() command: Name, age, house number, street name
name = input("Enter your name: ")
age = input("Enter your age: ")
house = input("Enter your house number: ")
street = input("Enter your street name: ")

# Print a single sentence containing all the information
print("This is {}.  He is {} years old, and lives at house number {} on {}".format(name, age, house, street))