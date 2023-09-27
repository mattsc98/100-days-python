import requests 

from flight_data import FlightData

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.read_sheety = 'https://api.sheety.co/938cf0496091dff68ea11077fd14c274/flightDeals/prices'

        
    def get_sheet_info(self):
        data = requests.get(self.read_sheety)
        sheet_info = data.json()
        
        self.flights = []
        for data in sheet_info['prices']:
            city = data["city"]
            iataCode = data["iataCode"]
            lowestPrice = data["lowestPrice"]
            
            self.flights.append(FlightData(city, iataCode, lowestPrice))
        
        return self.flights
    
                
    def put_sheet_data(self, flights):
        row = 2
        
        for flight in flights:
            
            sheety_input = {
                'price' : {
                    'iataCode' : flight.code
                }
            }
            
            put_sheet_endpoint = f'https://api.sheety.co/938cf0496091dff68ea11077fd14c274/flightDeals/prices/{row}'
            put = requests.put(put_sheet_endpoint, json=sheety_input)     
            row += 1
        
        


        