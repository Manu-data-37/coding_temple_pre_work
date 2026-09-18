# User input

destination = str(input('Enter your destination'))
distance = float(input('Enter distance in miles'))
car_fuel_gallon = float(input('car fuel efficiency per gallon?'))
gas_price = float(input('Current gas price per gallon?'))
number_of_nights = int(input('How many nights will you be staying?'))
number_of_nights = float(input('Average hotel cost per night'))
food_budget = float(input('What is your food budget?'))

# Calculations / Data Mnipulation
gas_needed = (distance / car_fuel_gallon)
gas_cost = (car_fuel_gallon * gas_price)
hotel_cost = (number_of_nights * number_of_nights)
cost_of_food = (number_of_nights + 1) * food_budget

# Grand total must be the sum o all cost
# Output must show 2 decimal places
costs = [cost_of_food, hotel_cost, gas_cost]
sum_of_costs = sum(costs)

# Display
print("=== Road Trip Planner ===") 
print("Destination: ", destination)
print("Distance: ", distance)
print("=== Cost Breakdown ===") 

print("Gas: ",)
print("Hotel: ")
print("Food: ")

print("_____" * 3)
print("Estinated Total", sum_of_costs)
