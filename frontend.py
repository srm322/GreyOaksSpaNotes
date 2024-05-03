import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Function to get the encryption key
def get_encryption_key():
    # Open enc key file
    with open("passwdEncryption/fernetkey.txt", 'rb') as file:
        #print(file.read())
        return file.read()

# Function to get the encrypted password
def get_encrypted_password():
    # Open enc passwd file
    with open("passwdEncryption/fernetpass.txt", 'r') as file:
        key = file.read()
        print(key)
        return key

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
        # Set focus to the password entry
        self.password_entry.focus_set()

        # Button to check the password
        self.submit_button = tk.Button(frame, text="Submit", command=self.check_password)
        self.submit_button.pack(side=tk.LEFT)

    def check_password(self):
        # Get the encryption key and encrypted password
        encryption_key = get_encryption_key()
        encrypted_password = get_encrypted_password()

        # Decrypt the password at runtime
        fernet = Fernet(encryption_key.decode())
        try:
            correct_password = fernet.decrypt(encrypted_password).decode()
        except Exception as e:
            print("Decryption error: ", str(e))

        # Check if the entered password matches the decrypted correct password
        if self.password_entry.get() == correct_password:
            # Navigate to the welcome screen
            self.open_welcome_screen()
        else:
            # Show error message
            messagebox.showerror("Error", "Wrong password!")
            # Clear the password field and set focus back
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus_set()

    def open_welcome_screen(self):
        # Destroy the password screen and open the welcome screen
        self.destroy()
        HomeScreen()

# Home screen class (remains the same)
class HomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Member Search")

        # Set the geometry for 800x600
        self.geometry("800x600")

        # Layout Frame
        layout_frame = tk.Frame(self)
        layout_frame.pack(pady=20, padx=20)

        # Search Label
        search_label = tk.Label(layout_frame, text="Search Members")
        search_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Search Bar
        self.search_entry = tk.Entry(layout_frame, width=40)
        self.search_entry.grid(row=1, column=0, padx=10)

        # Search Button
        search_button = tk.Button(layout_frame, text="Search", command=self.on_search)
        search_button.grid(row=1, column=1)

        # Toggle Frame
        toggle_frame = tk.Frame(layout_frame)
        toggle_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Option variable
        self.search_option = tk.StringVar(value="name")

        # Toggle Switch (Radiobuttons)
        search_by_name = tk.Radiobutton(
            toggle_frame, text="Search by Name", variable=self.search_option, value="name"
        )
        search_by_id = tk.Radiobutton(
            toggle_frame, text="Search by ID", variable=self.search_option, value="id"
        )

        search_by_name.pack(side="left", padx=10)
        search_by_id.pack(side="right", padx=10)

        # Quit button
        quit_button = tk.Button(self, text="Quit", command=self.quit)
        quit_button.pack(pady=10)

    def on_search(self):
        search_query = self.search_entry.get()
        search_type = self.search_option.get()

        # Example search logic
        if search_query:
            if search_type == "name":
                print(f"Searching by name: {search_query}")
            elif search_type == "id":
                print(f"Searching by ID: {search_query}")
        else:
            print("Please enter a search query.")

# Run the application
if __name__ in "__main__":
    app = PasswordApp()
    app.mainloop()