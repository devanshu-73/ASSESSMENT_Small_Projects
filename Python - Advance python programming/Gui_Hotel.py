import tkinter as tk
from HotelFunctions import HotelFunctions

class HotelGUI:
    def __init__(self):
        self.functions = HotelFunctions()
        self.screen = tk.Tk()
        self.screen.title("Hotel Management System")

        # Screen size
        self.screen.geometry("610x550")

        # Welcome Message
        welcome_label = tk.Label(self.screen, text="Welcome", font=("Helvetica", 30, "bold"))
        welcome_label.grid(columnspan=2)

        # Buttons (Left Part)
        button_frame = tk.Frame(self.screen)
        button_frame.grid(row=1, padx=20, pady=20)

        button_width = 15  # common width for all buttons

        check_in = tk.Button(button_frame, text="Check In", command=self.functions.check_in, font=("Helvetica", 16, "bold"), width=button_width)
        check_in.grid(pady=10)

        show_guest_list = tk.Button(button_frame, text="Show Guest List", command=self.functions.show_guest_list, font=("Helvetica", 16, "bold"), width=button_width)
        show_guest_list.grid(row=1, pady=10)

        check_out = tk.Button(button_frame, text="Check Out", command=self.functions.check_out, font=("Helvetica", 16, "bold"), width=button_width)
        check_out.grid(row=2, pady=10)

        get_guest_info = tk.Button(button_frame, text="Get Guest Info", command=self.functions.get_guest_info, font=("Helvetica", 16, "bold"), width=button_width)
        get_guest_info.grid(row=3, pady=10)

        exit_button = tk.Button(button_frame, text="Exit", command=self.screen.destroy, font=("Helvetica", 16, "bold"), width=button_width)
        exit_button.grid(row=4, pady=10)

        # Hotel Name (Right Part)
        name_label = tk.Label(self.screen, text="Tops Hotel\nManagement", font=("Helvetica", 40, "bold"))
        name_label.grid(row=1, column=1, padx=20, pady=20)

    def run(self):
        self.screen.mainloop()

if __name__ == "__main__":
    hotel_gui = HotelGUI()
    hotel_gui.run()
