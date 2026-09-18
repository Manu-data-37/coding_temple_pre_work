# User input

destination = str(input('Enter your destination: '))
distance = float(input('Enter distance in miles: '))
car_fuel_gallon = float(input('car fuel efficiency per gallon?: ' ))
gas_price = float(input('Current gas price per gallon?: '))
# variable name was repeated, had to fix it.
number_of_nights_staying = int(input('How many nights will you be staying?: '))
avg_hotel_cost = float(input('Average hotel cost per night: '))
food_budget = float(input('What is your food budget?: '))

# Calculations / Data Mnipulation
# Variables have been updated
gas_needed = distance / car_fuel_gallon
gas_cost = gas_needed * gas_price
hotel_cost = number_of_nights_staying * avg_hotel_cost
cost_of_food = (number_of_nights_staying + 1) * food_budget

# Grand total must be the sum o all cost

costs = [cost_of_food, hotel_cost, gas_cost]
sum_of_costs = sum(costs)

# Display
print("=== Road Trip Budget Planner ===") 
print(f'Destination: {destination}')
print(f'Distance: {distance:.2f} miles\n')


print("--- Cost Breakdown ---") 

print(f'Gas ({gas_needed:.2f} gal @ ${gas_price:.2f}/ gal): ${gas_cost:.2f}')
print(f'Hotel ({number_of_nights_staying} nights @ ${avg_hotel_cost:.2f}): ${hotel_cost:.2f}')
print(f'Food ({number_of_nights_staying+1} days @ ${food_budget:.2f}):      ${cost_of_food:.2f}')

print("-" * 29)
print(f'Estimated Total:       ${sum_of_costs:.2f}')
