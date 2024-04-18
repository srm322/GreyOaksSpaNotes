import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="GreyOaks2400"
)

print(mydb)