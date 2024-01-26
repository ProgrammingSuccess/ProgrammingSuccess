# Ask the user to enter three different integers.
first_number = int(input("Please enter an integer: "))
second_number = int(input("Thank you.  Now, please enter a second integer: "))
third_number = int(input("Finally, please enter a third integer: "))

# Then print out:
# The sum of all the numbers
total = (first_number + second_number + third_number)
print("The first number minus the second number is:" ,total)
# The first number minus the second number
first_minus_second = (first_number - second_number)
print("The third number multiplied by the first number is:" ,first_minus_second)
# The third number multiplied by the first number
third_times_first = (third_number * first_number)
print("The total of all the numbers you have entered is:" ,third_times_first)
# The sum of all three numbers divided by the third number
total_divided_by_third = (total / third_number)
print("The sum of all three numbers divided by the third number is:" ,total_divided_by_third)