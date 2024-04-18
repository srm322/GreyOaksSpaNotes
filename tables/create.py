import mysql.connector

# Function to establish database connection
def connect_to_database():
    return mysql.connector.connect(
        user='your_username',
        password='your_password',
        host='localhost',
        database='your_database'
    )

# Function to create tables
def create_tables(connection):
    cursor = connection.cursor()
    
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
    
    connection.commit()
    cursor.close()

# Function to insert sample data into tables
def insert_sample_data(connection):
    cursor = connection.cursor()
    
    # Insert sample members
    cursor.execute("INSERT INTO members (member_number, member_name) VALUES (1, 'John Doe')")
    cursor.execute("INSERT INTO members (member_number, member_name) VALUES (2, 'Jane Smith')")
    
    # Insert sample appointments
    cursor.execute("INSERT INTO appointments (member_number, appointment_date, appointment_notes) VALUES (1, '2024-04-20', 'Follow-up appointment')")
    cursor.execute("INSERT INTO appointments (member_number, appointment_date, appointment_notes) VALUES (2, '2024-04-21', 'Annual check-up')")
    
    connection.commit()
    cursor.close()

# Function to purge tables (drop tables)
def purge_tables(connection):
    cursor = connection.cursor()
    
    # Drop members table
    cursor.execute("DROP TABLE IF EXISTS members")
    
    # Drop appointments table
    cursor.execute("DROP TABLE IF EXISTS appointments")
    
    connection.commit()
    cursor.close()

# Establish database connection
connection = connect_to_database()

# Create tables
create_tables(connection)

# Insert sample data (optional)
insert_sample_data(connection)

# Purge tables (uncomment to use)
# purge_tables(connection)

# Close connection
connection.close()
print("Tables created successfully.")
