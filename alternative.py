#Write a program that reads in a string and makes each alternate
#character into an upper case character and each other alternate character
#a lower case character.
#e.g. The string “Hello World” would become “HeLlO WoRlD”

string = input("Please enter a string: ")
# User input for string

new_string = ""
string_list = []
# Empty string to add to

# Make each alternating character 
# of the string upper and lower case (e.g. HElLo)

for alternate in range(len(string)):

    if alternate % 2 == 0:
        new_string += string[alternate].upper()
        # If even, then makes character uppercase

    else:
        new_string += string[alternate].lower()
        # If odd, then makes character lowercase

# Output the first required element
print(f"The new string - with alternating letters in UPPER and lower case - is: {new_string}")

#Now, try starting with the same string but making each alternative word
#lower and upper case.
#e.g. The string: “I am learning to code” would become “i AM learning
#TO code”.
#Tip: Using the split() and join() functions will help you here

# Make each alternating word 
# of the string upper and lower case (e.g. HElLo)

split_word = string.split()

for alternate in range(len(split_word)):
# Split the input string into individual words

    if alternate % 2 == 0:
        string_list.append(split_word[alternate].lower())
        # If the word is odd, then it will be lower case
    else:
        string_list.append(split_word[alternate].upper())
        # If the word is even, then it will be upper case

# Check that we have split the string, word by word:
"""print(split_word)"""
# Check that we have changed the case of alternate words in the string, word by word:
"""print(string_list)"""

new_alt_string = " ".join(string_list)
# Combine the words back together, in a new string

# Output the second required element
print(f"The new string - with alternating words in UPPER and lower case - is: {new_alt_string}")