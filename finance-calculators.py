import math
# Create a program to allow a user to select an investment or a bond repayment calculator
# The user should be allowed to choose which calculation they want to do.
print("Which sort of calculation would you like me to do for you?")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
userEntry = (input("Enter either 'investment' or 'bond' from the menu above to proceed:"))
# How the user capitalises their selection should not affect how the program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’, ‘INVESTMENT’, etc., should all be recognised as valid entries. 
selection = userEntry.lower()
print(selection)

# If the user selects ‘investment’, do the following:
if selection == "investment":
# Ask the user to input:
# The amount of money that they are depositing.
    P = int(input("How much money are you depositing? :"))
# The interest rate (as a percentage). 
# Only the number of the interest rate should be entered — don’t worry about having to deal with the added ‘%’, e.g. The user should enter 8 and not 8%.
    rate = (input("What interest rate will you receive on your money? :"))
    newRate = rate.replace('%', ' ')
    rate = float(newRate)
    r = rate / 100
# The number of years they plan on investing.
    t = int(input("How many years do you plan to invest your money for? :"))
# Then ask the user to input if they want “simple” or “compound” interest
# Store this in a variable called interest. 
# Depending on whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back after the given period, at the specified interest rate. See below for the formula to be used:
    interest = (input("Do you want to calculate 'simple' or 'compound' interest on your deposited money? :"))
    if interest == "simple":
        A = P *(1 + r*t)
# Print out the answer!
        print("Calculating with a simple interest rate of {}, your initial investment of {} will be worth {} at the end of {} years.".format(rate, P, A, t))
    elif interest == "compound":
        A = P * ((1+r)**t)
# Print out the answer!
        print("Calculating with a compound interest rate of {}, your initial investment of {} will be worth {} at the end of {} years.".format(rate, P, A, t))
    else:
        print("I'm sorry, but you have to make a choice between either 'simple' or 'compound'.  Please try again.")

# If the user selects ‘bond’, do the following:
elif selection == "bond":
# Ask the user to input:
# The present value of the house. e.g. 100000
    P = int(input("What is the current value of the house? e.g. 100000 :"))
# The interest rate. e.g. 7
    rate = (input("What interest rate will you have to pay on your bond? e.g. 7 :"))
    newRate = rate.replace('%', ' ')
    rate = float(newRate)
    r = rate / 100
    i = r / 12
# The number of months they plan to take to repay the bond. e.g. 120
    n = int(input("How many months do you plan to take to repay the bond? e.g. 120 :"))
# Calculate how much money the user will have to repay each month and output the answer.
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print("You will have to repay {} per month.".format(repayment))

# If the user doesn’t type in a valid input, show an appropriate error message.
else:
    print("I'm sorry, but you have to make a choice between either 'investment' or 'bond'.  Please try again.")