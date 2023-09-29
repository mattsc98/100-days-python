import requests 

class Users():
    def __init__(self):
        self.post_sheety = 'https://api.sheety.co/938cf0496091dff68ea11077fd14c274/flightDeals/users'
        
    def add_user(self, name, lastname, email):
        user_data = {
            'user' : {
                'firstName' : name,
                'lastName'  : lastname,
                'email'     : email
            }
        }
        
        post_response = requests.post(self.post_sheety, json=user_data)
        print(post_response)