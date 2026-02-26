#To create a database
import mysql.connector
myconn=mysql.connector.connect(host="localhost", user="root", passwd="sql@45f3450mjz")
mycursor=myconn.cursor()
x=input("Enter the name for new database:")
mycursor.execute("create database "+x)
print("database created: "+x)
myconn.close()