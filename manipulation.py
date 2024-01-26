# Ask the user to enter a sentence using the input() method.
# Save the user’s response in a variable called str_manip.
str_manip = input("Enter a sentence: ")
# Using this string value, write the code to do the following:
# Calculate and display the length of str_manip.
length = len(str_manip)
penultimate = length - 1
# Find the last letter in str_manip sentence. 
last = str_manip [penultimate::]
print("This sentence is {} characters long.  The last character is {}".format(length, last))
# Replace every occurrence of this letter in str_manip with ‘@’. 
last_letter = str(last)
new_sentence = str_manip.replace(last_letter, '@')
print(new_sentence)
# Print the last 3 characters in str_manip backwards.
prepenultimate = penultimate -1
antiprepenultimate = penultimate - 3
print(str_manip[:antiprepenultimate:-1])
# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip.
first_three = str_manip [0:3]
last_two = str_manip [prepenultimate::]
five_letter_word = first_three+last_two
print(five_letter_word)