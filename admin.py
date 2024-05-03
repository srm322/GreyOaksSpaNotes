import mysql.connector
import csv

# Function to establish database connection
def connect_to_database():
    return mysql.connector.connect(
        user='root',
        password='GreyOaks2400',
        host='localhost',
        database='greyOaksNotes'
    )

#Just gonna initialte connection globally
connection = connect_to_database()
cursor = connection.cursor()
    

def optAddApt():
    
    return 0
    
print("Welcome to the Grey Oaks CC Spa Admin SQL Console\n:) :D :)\n\n")

print("If you can run it, you're qualified (plus I don't want to make an authentication procedure rn)")

print("Options:\n1. Refresh Tables\n2. Refresh Member Database\n3. **\n")
sel = input("Option? : ")

if sel == 1:
    # Create members table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            member_number INT PRIMARY KEY,
            member_name VARCHAR(255) NOT NULL
        )
    """)
    
    # Create appointments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INT AUTO_INCREMENT PRIMARY KEY,
            member_number INT,
            appointment_date DATE NOT NULL,
            appointment_notes TEXT,
            FOREIGN KEY (member_number) REFERENCES members(member_number)
        )
    """)

if sel == 2:
    # Read CSV data
    with open("yourfile.csv", 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Skip the header

        # Insert data into MySQL table
        for row in csv_reader:
            cursor.execute(
                "INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)",
                row
            )

# Commit the transaction and close the connection
connection.commit()
cursor.close()
connection.close()
