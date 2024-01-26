# Imagine you are running a cafe. Create a new Python file in your folder
# called cafe.py.
# ● Create a list called menu, which should contain at least four items sold in
# the cafe.
menu = ['Americano', 'Mocha', 'Cappuccino', 'Muffin', 'Cookie']

# ● Next, create a dictionary called stock, which should contain the stock value for each item on your menu.
# This instruction seems poorly expressed, or at least could be clearer, but I will interpret it as:
# "Create a dictionary called stock, which should contain the number in stock of each item on your menu"
# [Explanation: the 'stock value' is not the same as the number of items in stock.  
# The 'stock value' (in a real world setting) would be more like the 'wholesale cost' of each item]
# If my interpretation of what is intended by the instruction is incorrect, then please let me know
stock = [50, 50, 50, 100, 100]

# To combine these two lists as a dictionary
items_in_stock = list(zip(menu,stock))
# Check that these lists have been combined correctly
print("Number of each menu item in stock:", items_in_stock)

# Having said that the 'stock value' is not the same as the 'number of items in stock', 
# it would also be possible to create a list of the 'wholesale costs' of each item.
# This would be useful for working out the profit margin on each item, and "the profitability of the cafe overall
# (assuming that every item was sold, of course)
wholesale_costs = [1, 2, 2, 2, 1]
# https://datagy.io/python-multiply-lists/#Multiply%20Two%20Python%20Lists%20Element-Wise%20Using%20Numpy
# Find out what has been spent on stocking the cafe:
stock_values  = [item1 * item2 for item1, item2 in zip(stock, wholesale_costs)]
# Check that these lists have been combined correctly
"""print(stock_values)"""
# https://stackoverflow.com/questions/13909052/how-do-i-add-together-integers-in-a-list-sum-a-list-of-numbers-in-python
# returns: [(50 x 1 =) 50, (50 x 2 =) 100, (50 x 2 =) 100, (100 x 2 =) 200, (100 x 1 =) 100]

# Or, more meaningfully, to combine the list of stock_values with the list of items
# https://stackoverflow.com/questions/7271385/how-do-i-combine-two-lists-into-a-dictionary-in-python
stock_values_in_stock = list(zip(menu,stock_values))
print("Cost of each menu item in stock:", stock_values_in_stock)

# Finally, to have a total value of stock on hand (money invested in stock):
total_stock_value = sum(stock_values)
print("Total cost of stock:", total_stock_value)
# returns: [(50 + 100 + 100 + 200 + 100 = ) 550]

# ● Create another dictionary called price, which should contain the prices for each item on your menu.
prices = [2, 3, 3, 3, 2]
price_list = list(zip(menu,prices))
print("Price list:", price_list)

# ● Next, calculate the total_stock worth in the cafe. You will need to
# remember to loop through the appropriate dictionaries and lists to do this.
stock_worth  = [item1 * item2 for item1, item2 in zip(stock, prices)]
# Check that these lists have been combined correctly
"""print(stock_worth)"""
# returns: [(50 x 2 =) 100, (50 x 3 =) 150, (50 x 3 =) 150, (100 x 3 =) 300, (100 x 2 =) 200]

# Or, more meaningfully, to combine the list of stock_worth with the list of items
stock_worth_in_stock = list(zip(menu,stock_worth))
print("Price of each menu item in stock:", stock_worth_in_stock)

total_stock_worth = sum(stock_worth)
print("Total worth of stock:", total_stock_worth)
# returns: [(100 + 150 + 150 + 300 + 200 = ) 900]

# I am not very comfortable with the way in which the terms 'value' and 'worth' are used in this task,
# though I have tried to keep close to the ways in which they are used in the instruction,
# whilst trying to remain clear.
# In a real world retail setting, I think terms like 'value' would more usually be used
# with the final output, rather than 'Total worth of stock' (which is taken from the task instruction:
# 'calculate the total_stock worth in the cafe'), I would have preferred 'Total sales value of stock'.
# Anyway.

# As set out, the profitability (assuming that every item is sold) of the cafe could be calculated

# Profitability per item
profit_margin_per_item = [item1 - item2 for item1, item2 in zip(prices, wholesale_costs)]
# Check that these lists have been combined correctly
"""print(profit_margin_per_item)"""
# returns: [(2 - 1 =) 1, (3 - 2 =) 1, (3 - 2 =) 1, (3 - 2 =) 1, (2 - 1 =) 1]

# Or, more meaningfully, to combine the list of profit_margin_per_item with the list of items
stock_profit_by_item = list(zip(menu, profit_margin_per_item))
print("Profit for each menu item in stock:", stock_profit_by_item)

# Profitability overall
total_profit_margin = total_stock_worth - total_stock_value
print("Overall potential profit:", total_profit_margin)

# This could then be further extended, to calculate the rate of profitability 
# (still assuming that every item is sold) of the cafe 

# Of course, this assumes that overhead costs, heat/light/power, staffing, etc. have all been incorporated
# into the 'cost' of each menu item.
# So, in the end, this isn't a true reflection of the cafe's profitability.  Ah well!