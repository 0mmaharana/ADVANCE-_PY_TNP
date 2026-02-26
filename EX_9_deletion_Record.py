#Deleting one record
import mysql.connector

myconn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db5"
)
mycursor = myconn.cursor()
sql = "DELETE FROM employee WHERE id = 10"
mycursor.execute(sql)
myconn.commit()
print(mycursor.rowcount, "record(s) deleted")
