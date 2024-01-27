# Customer.py
class Customer:
    def __init__(self, name, contact, email, gender, city, state):
        self.name = name
        self.contact = contact
        self.email = email
        self.gender = gender
        self.city = city
        self.state = state

    def display_details(self):
        print(f' Name : {self.name}')
        print(f' Contact : {self.contact}')
        print(f' Email : {self.email}')
        print(f' Gender : {self.gender}')
        print(f' City : {self.city}')
        print(f' State : {self.state}')
