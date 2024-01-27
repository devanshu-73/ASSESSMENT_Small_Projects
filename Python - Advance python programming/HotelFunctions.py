# HotelFunctions.py
import tkinter as tk
from tkinter import ttk
from Manager import HotelManager
from RegistrationForm import RegistrationForm

class HotelFunctions:
    def __init__(self):
        self.manager = HotelManager()

    def check_in(self):
        root = tk.Tk()
        registration_form = RegistrationForm(root, self.manager)
        root.mainloop()

    def show_guest_list(self):
        self.manager.display_customers()

    def check_out(self):
        print("check_out")

    def get_guest_info(self):
        print("get_guest_info")
