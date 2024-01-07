# import tkinter as tk
# from HotelFunctions import HotelFunctions

# class HotelGUI:
#     def __init__(self):
#         self.functions = HotelFunctions()
#         self.screen = tk.Tk()
#         self.screen.title("Hotel Management System")

#         # Configure window size
#         self.screen.geometry("610x550")  # Adjust the size as needed

#         # Welcome Message
#         welcome_label = tk.Label(self.screen, text="Welcome", font=("Helvetica", 30, "bold"))
#         welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

#         # Buttons (Left Part)
#         button_frame = tk.Frame(self.screen)
#         button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="w")

#         button_width = 15  # Set a common width for all buttons

#         check_in_button = tk.Button(button_frame, text="Check In", command=self.functions.check_in, font=("Helvetica", 16, "bold"), width=button_width)
#         check_in_button.grid(row=0, column=0, pady=10, sticky="w")

#         show_guest_list_button = tk.Button(button_frame, text="Show Guest List", command=self.functions.show_guest_list, font=("Helvetica", 16, "bold"), width=button_width)
#         show_guest_list_button.grid(row=1, column=0, pady=10, sticky="w")

#         check_out_button = tk.Button(button_frame, text="Check Out", command=self.functions.check_out, font=("Helvetica", 16, "bold"), width=button_width)
#         check_out_button.grid(row=2, column=0, pady=10, sticky="w")

#         get_guest_info_button = tk.Button(button_frame, text="Get Guest Info", command=self.functions.get_guest_info, font=("Helvetica", 16, "bold"), width=button_width)
#         get_guest_info_button.grid(row=3, column=0, pady=10, sticky="w")

#         exit_button = tk.Button(button_frame, text="Exit", command=self.screen.destroy, font=("Helvetica", 16, "bold"), width=button_width)
#         exit_button.grid(row=4, column=0, pady=10, sticky="w")

#         # Hotel Name (Right Part)
#         name_label = tk.Label(self.screen, text="Tops Hotel\nManagement", font=("Helvetica", 40, "bold"))
#         name_label.grid(row=1, column=1, padx=20, pady=20, sticky="e")  # Use sticky to align to the right

#     def run(self):
#         self.screen.mainloop()

# if __name__ == "__main__":
#     hotel_gui = HotelGUI()
#     hotel_gui.run()
