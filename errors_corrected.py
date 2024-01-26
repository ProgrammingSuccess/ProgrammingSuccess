# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Notes added in the lines after each correction which has been made (multiple notes on multiple lines, where more than one correction type in a line)

program_name = "Welcome to the error program"
#Logical error: the purpose here is to allocate the text "Welcome to the error program" to a variable, 
#so that the program can print that variable later.
#Syntax error: variable should not begin with a forward slash (\)
#Naming convention not met ('n').  Better to have a variable name which is more meaningful, such as 'Program_Name'.
print(program_name)
#Incorrect space indentation, needs to be in line with 'print', in the line above
#Syntax error: needs to be in brackets, with no space after 'print'
#Syntax error: once the variable has been allocated, no "" are required around it, within the brackets

    # Variables declaring the user's age, casting the str to an int, and printing the result
""" age_Str = "24 years old" """
#Incorrect indentation
#Syntax error: only one "=" required
#Logical error: the variable "24 years old", as a mixture of text and number, cannot easily be cast to an integer 
#(without separating the number from the other text).
""" age = int(age_Str) """
#Incorrect indentation

#Error of limited thinking in this whole section, above.
#In this format, where "age" is pre-assigned, the program is limited to that one pre-assigned number. 
#More meaningful to have a variable, where the user is asked to enter their age.
#Improvement is to ask the user to insert their age in years, followed by the number of additional months (e.g. 24 years and 6 months)
age_years = int(input("Please enter your age in years, as an integer: "))
age_months = int(input("Thank you.  Now, please tell me how many months you are older than that [enter 0, if you are exactly that age]: "))

print("So you are ", age_years, "years and", age_months, "months old")
#Incorrect indentation
#Syntax error: the text to be printed and the variables need to be separated by a comma and a space, not by "+"
#User-friendly error - makes more sense for the computer to refer to the user as 'you', so it appears more conversational.

#To make the rest of the program more meaningful (and the final outcome of months more meaningful)
#it would make sense to add in a section here which calculates the user's current age in months:
current_age_months = (age_years * 12) + age_months
print("Another way of looking at this, is that you are currently", current_age_months, "months old")

    # Variables declaring additional years and printing the total years of age
""" years_from_now = "3" """
#Incorrect indentation
#Again, limited thinking, because the program will be limited to only that one additional period of 3 years.
#More meaningful to have a variable, where the user is asked to enter a period of additional years.
print("O.K. Let's think about how many months old you will be, by a certain number of years from now.")
#Offer some user-friendly text, to explain what is happening
years_from_now = int(input("Please enter a number of years into the future, as an integer: "))

print("Perhaps you would like to add an additional number of months, to this number of years ... ")
#Offer some user-friendly text, to explain what is happening
months_from_now = int(input("Please enter a number of additional months into the future, as an integer: "))
#Now we have a user-friendly interaction, which allows for the flexibility of adding any number of years and months into the future.

""" total_years = age + years_from_now"""
#Incorrect indentation

#Given the wider range of variables which the user can now select (their age, in years and months; a number of years and months into the future)
#we need a slightly more complicated way of adding up all the different bits.
#We could add in a way of adding the number of months 'age_months' and 'months_from_now', to convert to a total number of years
#However, given that the program is actually aiming merely to convert the total of years and months all to months, this seems unneccessary.
#Therefore, let's take this next line out of the program:
"""print("The total number of years:" + total_years)"""
#Syntax error: needs to be in brackets, with no space after 'print'
#Logical error: the 'total number of years' will be the variable 'total_years', not the text 'answer_years')

#Instead, let's calculate the total number of years
total_years = age_years + years_from_now
#and the total number of months
total_months = age_months + months_from_now

# Variable to calculate the total amount of months from the total amount of years and printing the result
"""total_months = total_years * 12"""
#Logical error: 'total_months' will be the variable 'total_years', not the (unidentified) variable 'total'
#Given the changes above, this now needs to be re-cast as:
total_months = (total_years * 12) + total_months

"""print("In 3 years and 6 months, I'll be " + total_months + " months old")"""
#Syntax error: needs to be in brackets, with no space after 'print'
#Again, the conversational exchange makes more sense if we make this output refer to 'you' (rather than 'I'), and tweak this to:
print("In", years_from_now, "years and", months_from_now, "months from now, you will be", total_months, "months old.")

#HINT, 330 months is the correct answer
#This now provides this answer, if the user enters their age as '24', and selects '3' additional years and '6' additional months.
#This is also more flexible, as it offers the user the opportunity to calculate their age in months now, 
#and at any number of years and months from now.

#Additional options would be to add in a check for whether the user entered an integer when requested so to do.
#e.g.
"""
try:
    a = int(age_years)
    print("Thank you")
except:
    print("You have not entered a number.  Please try again.")
"""
