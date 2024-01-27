# Manager.py
from DB_Connection import Database
from Customer import Customer

class HotelManager:
    def __init__(self):
        self.db = Database()  # Database Object as db
        self.create_customers_table()

    def create_customers_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                contact VARCHAR(20) NOT NULL,
                email VARCHAR(255) NOT NULL,
                gender VARCHAR(10) NOT NULL,
                city VARCHAR(50) NOT NULL,
                state VARCHAR(50) NOT NULL
            )
        """
        self.db.execute_query(query)
        print("Customers table created or already exists.")

    def add_customer(self, name, contact, email, gender, city, state):
        
        customer = Customer(name, contact, email, gender, city, state)
        
        # Insert customer_details into the database
        
        query = "INSERT INTO customers (name, contact, email, gender, city, state) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, contact, email, gender, city, state)
        self.db.execute_query(query, values)
        print("Customer added successfully!")

    def display_customers(self):
        query = "SELECT * FROM customers"
        customers = self.db.fetch_data(query)
        for customer in customers:
            print(customer)
