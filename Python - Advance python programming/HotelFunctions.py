import tkinter as tk
from tkinter import ttk
from Manager import HotelManager

class RegistrationForm:
    def __init__(self, master, manager):
        self.master = master
        self.master.title("Registration Form")
        self.manager = manager

        # Variables to store user inputs
        self.name_var = tk.StringVar()
        self.contact_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="Male")
        self.city_var = tk.StringVar()
        self.state_var = tk.StringVar()

        self.create_form()

    def on_radio_select(self):
        selected_gender = self.gender_var.get()
        print("Selected Gender: ", selected_gender)

    def create_form(self):
        # Name
        self.label_name = tk.Label(self.master, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.master, textvariable=self.name_var)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        # Contact
        self.label_contact = tk.Label(self.master, text="Contact:")
        self.label_contact.grid(row=1, column=0, padx=10, pady=5)
        self.entry_contact = tk.Entry(self.master, textvariable=self.contact_var)
        self.entry_contact.grid(row=1, column=1, padx=10, pady=5)

        # Email
        self.label_email = tk.Label(self.master, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(self.master, textvariable=self.email_var)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        # Gender
        self.label_gender = tk.Label(self.master, text="Gender:")
        self.label_gender.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.radio_male = tk.Radiobutton(self.master, text="Male", variable=self.gender_var, value="Male",
                                         command=self.on_radio_select)
        self.radio_male.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        self.radio_female = tk.Radiobutton(self.master, text="Female", variable=self.gender_var, value="Female",
                                           command=self.on_radio_select)
        self.radio_female.grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)

        # City
        self.label_city = tk.Label(self.master, text="City:")
        self.label_city.grid(row=4, column=0, padx=10, pady=5)
        cities = ["City1", "City2", "City3", "City4", "City5"]
        self.dropdown_city = ttk.Combobox(self.master, textvariable=self.city_var, values=cities)
        self.dropdown_city.grid(row=4, column=1, padx=10, pady=5)

        # State
        self.label_state = tk.Label(self.master, text="State:")
        self.label_state.grid(row=5, column=0, padx=10, pady=5)
        states = ["State1", "State2", "State3", "State4", "State5"]
        self.dropdown_state = ttk.Combobox(self.master, textvariable=self.state_var, values=states)
        self.dropdown_state.grid(row=5, column=1, padx=10, pady=5)

        self.register_button = tk.Button(self.master, text="Register", command=self.register)
        self.register_button.grid(row=6, column=0, columnspan=2, pady=10)

    def register(self):
        # Collect information from the form
        name = self.entry_name.get()
        contact = self.entry_contact.get()
        email = self.entry_email.get()
        gender = self.gender_var.get()
        city = self.dropdown_city.get()
        state = self.dropdown_state.get()

        print(f' Name : {name}')
        print(f' Contact : {contact}')
        print(f' Email : {email}')
        print(f' Gender : {gender}')
        print(f' City : {city}')
        print(f' State : {state}')

        try:
            success = self.manager.add_customer(name, contact, email, gender, city, state)
            if success:
                print("Customer added successfully!")
        except Exception as e:
            print(f"Error during registration: {e}")

        self.master.destroy()


class HotelFunctions:
    def __init__(self):
        self.manager = HotelManager()

    def check_in(self):
        root = tk.Tk()
        registration_form = RegistrationForm(root, self.manager)
        root.mainloop()

    def show_guest_list(self):
        self.manager.display_customers() # Displaying in in terminal

    def check_out(self):
        print("check_out")

    def get_guest_info(self):
        print("get_guest_info")
