# Write code to take in a user’s age and store it in an integer variable called age.
age = int(input("Please enter your age: "))
# Assume that the oldest someone can be is 100; if the user enters a higher number, output the message "Sorry, you're dead.".
if age >= 100: # Don’t forget the colon!
    print("Sorry, you are dead.")
# If the user is 65 or older, output the message "Enjoy your retirement!"
elif age >= 65: # Don’t forget the colon!
    print("Enjoy your retirement!")
# If the user is 40 or over, output the message "You're over the hill."
elif age >= 40: # Don’t forget the colon!
    print("You're over the hill!")
# If the user is under 13, output the message "You qualify for the kiddie discount."
elif age <= 13: # Don’t forget the colon!
    print("You qualify for the kiddie discount!")
# If the user is 21, output the message "Congrats on your 21st!"
elif age == 21: # Don’t forget the colon!
    print("Congratulations on your 21st!")
# For any other age, output the message "Age is but a number."
else: # Don’t forget the colon!
    print("Age is but a number")
