# This program calculates the total cost of a holiday by inputed information by the user, including: plane cost,
# hotel cost, and car rental cost. 

import math

print("<<Holiday calculator>>")
print("\nThis program will calculate the total cost of your next holiday.")
print("\nFlight Options: ")

city_flight_option = ['Madrid', 'Lisbon', 'Paris', 'Vienna', 'Recife']
print("\n".join(city_flight_option))

# Defining functions that will be used to calculate the holiday total cost, using user inputs.
def hotel_cost(num_nights):
    total_hotel_cost = num_nights * 180
    return total_hotel_cost

def plane_cost(city_flight):
    if city_flight == 'Madrid':
        plane_value = 330
    
    elif city_flight == 'Lisbon':
        plane_value = 450
    
    elif city_flight == 'Paris':
        plane_value = 630
    
    elif city_flight == 'Vienna':    
        plane_value = 800
    
    elif city_flight == 'Recife':
        plane_value = 1500
    
    return plane_value

def car_rental(rental_days):
    car_value = rental_days * 80
    return car_value

def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_holiday_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_holiday_cost

# Repeats the code block that calculates the holiday costs, until the user inputs 'q' as a city option.
while True:
    city_flight = input("\nPlease enter the city you'll be flighting to, from the above list (q=quit): ")
    if city_flight == 'q':
        break
    elif city_flight not in city_flight_option:
        print("Please enter a valid city from the list!")
        continue

    num_nights = int(input("Please enter the number of nights you'll be staying at the hotel: "))
    rental_days = int(input ("How many days will you be hiring the car? "))
    total_cost = holiday_cost(hotel_cost, plane_cost, car_rental ) # The variable that stores the cost of the holiday, calling the function holiday_cost.

    # Print out all the details about the holiday.
    print(f"\nThe total cost to travel to {city_flight}, for {num_nights} nights, renting a car for {rental_days} days is: {str(total_cost)}.")