class Base:
    def __init__(self, name, age, gender, balance):
        self.name = name
        self.age = age
        self.gender = gender
        self._balance = balance  # Private field

    def display_details(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nBalance: {self._balance}")

class Customer(Base):
    def __init__(self, name, age, gender, balance, room_number):
        super().__init__(name, age, gender, balance)
        self.room_number = room_number

    def display_details(self):
        super().display_details()
        print(f"Room Number: {self.room_number}")
