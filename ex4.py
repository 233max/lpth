# car amounts
cars = 100
# space size in a car
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# cars not been driven (in carpool)
cars_not_driven = cars - drivers
# cars been driven out
cars_driven = drivers
# capacity of the carpool
carpool_capacity = cars_driven * space_in_a_car
# average passengers in each car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")