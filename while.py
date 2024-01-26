# Write a program that continually asks the user to enter a number.
# Make use of the while loop repetition structure to implement the program.
# Set initial variables 'total' and 'iterations' to zero.
total = 0
iterations = 0

# First feedback asked for a statement informing the user to enter '-1' in order to break the loop, indicating this was a task requirement.  Although this is not actually in the task requirement (as set out in "Control Structures - While Loop"), this is now included here (and below, when the user is asked to enter the second and subsequent numbers).
print("This program will calculate the average of all the numbers you enter, until you enter -1 [The -1 will not be included in the average].")
number = int(input("Please enter a number: "))

# First feedback asked for a check that -1 was not entered as the first number
if number == -1 :
    print("There is no average to calculate.  You have entered -1, which ends the program, but no other numbers.")
else:

    while number != -1 :
# The variable 'total' records the running total of all the numbers which the user has entered.
        total = number + total
# The variable 'iterations' records the number of different numbers which the user has entered.
        iterations = iterations + 1
        number = int(input("Please enter another number [or -1 to let me know that this is the end of the list, and I will calculate the average of all the numbers you have already entered]: "))
# When the user enters “-1”, the program should stop requesting the user to enter a number
    if number == -1:
# The program must then calculate the average of the numbers entered, excluding the -1.
        average = total / iterations
        print("The average of all the numbers you have entered is: {}.".format(average))
