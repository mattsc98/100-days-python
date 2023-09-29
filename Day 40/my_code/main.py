#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from users import Users

from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "MLA"

# first_name = input("Enter your first name:\n")
# last_name = input("Enter your last name:\n")
# email = input("Enter your email:\n")
# email2 = input("Enter your email again:\n")

# while email != email2:
#     email = input("Emails do not match, enter your email:\n")
#     email2 = input("Enter your email again:\n")
# print("Welcome to the flight club!")

# users = Users()

# users.add_user(first_name, last_name, email2)

data_manager = DataManager()
flight_search = FlightSearch()

flights = data_manager.get_sheet_info()

sheets_put = False
for flight in flights:
    if flight.code == '':
        sheets_put = True
        flight.code = flight_search.get_iata_code(flight.city)

if sheets_put:
    data_manager.put_sheet_data(flights)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for flight in flights:
    price = flight_search.check_flights(ORIGIN_CITY_IATA, flight.code, tomorrow, six_month_from_today)
    
    ##send sms here