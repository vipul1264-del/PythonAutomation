import pyodbc
import mysql.connector as connector

connString = "Driver {Mysql}, SERVER=localhost, Database=student, username=root, password=admin"

try:
    conn = pyodbc.connect(connString)
    print("connected to DB")
except Exception as e:
    print(f"error while connection to DB ::{str(e)}")

# prepare the  query
query = "select * from marks"

try:
    cursor = conn.Cursor()
    rows = cursor.execute(query)
    for i in rows:
        print(i)
        print(i[1])
except Exception as e:
    print(f"error is :: {str(e)}")
