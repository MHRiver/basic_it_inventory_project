import mysql.connector #this is the library that allows us to connect to MySQL databases

db = mysql.connector.connect(   #checking to see if we can connect to the database 
    host="127.0.0.1",   #the db variable is now a connection object that we can use to interact with the database
    user="inventory_app",
    port = 3306,
    password="mhriver",
    database="it_inventory"
)

print("Connected to MySQL!") #print a message to the console to confirm the connection

cursor = db.cursor() #create a cursor object that we can use to execute SQL queries

cursor.execute("show tables;") #execute a SQL query to show the tables in the database

for table in cursor:
    print(table[0]) #print the name of each table in the database

cursor.close() #close the cursor object to free up resources


db.close() #close the connection to the database to free up resources
