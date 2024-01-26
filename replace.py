# Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.” as a single string.
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence)
# Reprint this sentence as “The quick brown fox jumps over the lazy dog.” using the replace() function to replace every “!” exclamation mark with a blank space.
new_sentence = sentence.replace('!', ' ')
print(new_sentence)
# Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.” using the upper() function
upper_sentence = new_sentence.upper()
print(upper_sentence)
# Print the sentence in reverse. (Hint: review what you learned about slicing!)
print(new_sentence[::-1])