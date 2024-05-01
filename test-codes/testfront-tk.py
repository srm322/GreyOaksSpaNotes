import tkinter as tk
from tkinter import messagebox

# Main Application class
class PasswordApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Screen")

        # Frame for password input
        frame = tk.Frame(self)
        frame.pack(pady=20)

        # Label and Entry for password
        self.label = tk.Label(frame, text="Enter Password:")
        self.label.pack(side=tk.LEFT)
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.pack(side=tk.LEFT, padx=10)

        # Button to check the password
        self.submit_button = tk.Button(frame, text="Submit", command=self.check_password)
        self.submit_button.pack(side=tk.LEFT)

    def check_password(self):
        # Correct password
        correct_password = "open"

        if self.password_entry.get() == correct_password:
            # Navigate to the welcome screen
            self.open_welcome_screen()
        else:
            # Show error message
            messagebox.showerror("Error", "Wrong password!")

    def open_welcome_screen(self):
        # Destroy the password screen and open the welcome screen
        self.destroy()
        WelcomeScreen()

# Welcome screen with a specific size
class WelcomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome Screen")

        # Set the geometry for 800x600
        self.geometry("800x600")

        # Welcome label
        welcome_label = tk.Label(self, text="Welcome!", font=("Arial", 24))
        welcome_label.pack(pady=20)

        # Quit button
        quit_button = tk.Button(self, text="Quit", command=self.quit)
        quit_button.pack(pady=10)

# Run the application
if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()
