import mysql.connector

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

print("Options:\n1. Add Appointment Notes\n2. Remove Apointment Notes")
sel = input("Option? : ")

