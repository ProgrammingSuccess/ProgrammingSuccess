# Your task will be to calculate a user’s total holiday cost, which includes 
# the plane cost, hotel cost, and car-rental cost.

# Get input from user
print("This program will calculate how much your holiday plans will cost.")
# Ask the user to enter three different variables.
city = input("\n1. Paris\n2. Rome\n3. Madrid\n4. Berlin\n0. Quit\nWhere are you flying to?  (Please type the full name of the city) ")
nights = int(input("How many nights will you be staying? "))
days = int(input("How many days will you need a car? "))

# Create lists to record cities, flight costs to each city,
# and hotel prices and car rental prices in each city

# Create a flight price list to each city
def flight_cost(city):
    flight_cost_dict = {"Paris": 250, "Rome": 300, "Madrid": 275, "Berlin":250}
    flight_cost = flight_cost_dict[city]
    return flight_cost
# To print the cost of flying to the selected city
print("The cost of your flight will be £",flight_cost(city))

# Create a hotel price list by city
def hotel_cost(nights, city):
    hotel_cost_dict = {"Paris": 200, "Rome": 150, "Madrid": 130, "Berlin":170}
    hotel_cost = hotel_cost_dict[city] * nights
    return hotel_cost
# To print the cost of staying for the selected number nights in a hotel in the selected city
print("The cost of your hotel will be: £",hotel_cost(nights, city))

# Create a carhire price list by city
def carhire_prices(days, city):
    carhire_prices_dict = {"Paris": 75, "Rome": 65, "Madrid": 60, "Berlin":70}
    carhire_prices = carhire_prices_dict[city] * days
    return carhire_prices
# To print the cost of renting a car for the selected number of days in the selected city
print("The cost of your carhire will be: £",carhire_prices(days, city))

# Calculate the cost of the holiday, # by combining the three different costs
holiday_cost = flight_cost(city) + carhire_prices(days, city) + hotel_cost(nights, city)

# Print the cost of the proposed holiday
print("The cost of your holiday will be: £",holiday_cost)