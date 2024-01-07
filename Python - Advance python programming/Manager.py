from DB_Connection import Database
from Customer import Customer

class HotelManager:
    def __init__(self):
        self.db = Database() # Database Object as db

    def add_customer(self, name, age, gender, balance, room_number):
        customer = Customer(name, age, gender, balance, room_number)
        query = "insert into customers (name, age, gender, balance, room_number) values (%s, %s, %s, %s, %s)"
        values = (customer.name, customer.age, customer.gender, customer._balance, customer.room_number)
        self.db.execute_query(query, values)
        print("Customer added successfully!")

    def display_customers(self):
        query = "select * from customers"
        customers = self.db.fetch_data(query)
        for customer in customers:
            print(customer)

# You can add more methods for other functionalities
