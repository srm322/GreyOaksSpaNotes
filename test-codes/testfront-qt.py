import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)

# Password screen with PyQt5
class PasswordApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window size
        self.setFixedSize(300, 150)
        self.setWindowTitle("Password Screen")

        # Layout for the widgets
        layout = QVBoxLayout()

        # Label and Line Edit for password
        self.label = QLabel("Enter Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        # Button to check the password
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_password)

        # Add widgets to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def check_password(self):
        # Correct password
        correct_password = "open"

        if self.password_entry.text() == correct_password:
            # Navigate to the welcome screen
            self.open_welcome_screen()
        else:
            # Show error message
            QMessageBox.critical(self, "Error", "Wrong password!")

    def open_welcome_screen(self):
        # Create the welcome screen
        self.close()
        welcome_screen = WelcomeScreen()
        welcome_screen.show()


# Welcome screen with PyQt5
class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window size
        self.setFixedSize(800, 600)
        self.setWindowTitle("Welcome Screen")

        # Layout for the widgets
        layout = QVBoxLayout()

        # Welcome label
        welcome_label = QLabel("Welcome!")
        layout.addWidget(welcome_label)

        # Quit button
        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(self.close)

        # Add widgets to the layout
        layout.addWidget(quit_button)

        self.setLayout(layout)


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    password_app = PasswordApp()
    password_app.show()
    sys.exit(app.exec_())
