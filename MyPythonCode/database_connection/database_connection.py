# database connection

# pip install mysql-connector-python

import mysql.connector as connector

try :
    con = connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "admin",
                database = "student"
                                    )  #connection successfully connected
    print("connected to DB")

except Exception as e:
    print(f"error while DB connection is :: {str(e)}")

try:
    query = "select * from marks where id = 4" #this is our mysql query
    cursor = con.cursor() # this is the object of the cursor which help us to perform the actions in DB
    cursor.execute(query)
    for value in cursor:
        print(value)
        subject = value[1]
        marks = value[2]
        print(f"subject of 4 is ::  {subject} \nmarks is ::  {marks}")

   
    # con.close() # it will disconnect the connection from DB
except Exception as e:
    print(f"error while DB connection is ::  { str(e)}")

# print("")

con.close()
print("connection is disconnect from DB")
