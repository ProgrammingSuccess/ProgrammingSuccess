# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"
#The variable 'animal' is being given the input 'Lion', but this should be entered in quotation marks to store it as a string.  
animal_type = "cub"
number_of_teeth = str(16)
#The variable 'number of teeth' should to be stored as an integer 
#(in case it is needed for calculations such as the number of additional teeth in an adult)

full_spec = "This is a", animal, ". It is a", number_of_teeth, " and it has", animal_type, "teeth"
#Logical errors.  The 'number_of_teeth' variable and 'animal_type' variable should be switched, above
#Syntax errors.  Need additional quotation marks and commas between the text and the variable to be printed.

#However, this step is simply not required, and the concatenation can be encapsulated in the PRINT statement, below:
print("This is a", animal, ". It is a", animal_type, ", and it has", number_of_teeth, "teeth")
#NB: A comma has been added to the print statement, after 'animal_type', to improve the English of the final statement