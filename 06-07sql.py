#To show tables present in a database

import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=myconn.cursor()

'''show all the databases'''
mycursor.execute("show databases")
db=mycursor.fetchall()
for i in db:
    print(i)

x=input("enter a database name")
mycursor.execute("use "+x)  #opening a database
mycursor.execute("show tables")#showing tables within a database

dbs=mycursor.fetchall()

print("tables are")
for i in dbs:
    print(i)