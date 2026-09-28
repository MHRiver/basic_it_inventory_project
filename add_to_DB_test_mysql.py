import mysql.connector #this is the library that allows us to connect to MySQL databases


# The fields in the table devices are as follows:
# - id: an integer that is the primary key for the table
# - name: a string that is the name of the device
# - device_type: a string that is the type of device (e.g. laptop, desktop, server, etc.)
# - ip_address: a string that is the IP address of the device
# - location: a string that is the location of the device



db = mysql.connector.connect(   #checking to see if we can connect to the database 
    host="127.0.0.1",   #the db variable is now a connection object that we can use to interact with the database
    user="inventory_app",
    port = 3306,
    password="mhriver",
    database="it_inventory"
)

print("Connected to MySQL!") #print a message to the console to confirm the connection

cursor = db.cursor() #create a cursor object that we can use to execute SQL queries

cursor.execute("""
    INSERT INTO devices (id, name, device_type, ip_address, location)
    VALUES (1, 'My Laptop', 'Laptop', '192.168.1.100', 'Dorm Room')
""")

db.commit() #commit the changes to the database so that they are saved

cursor.close() #close the cursor object to free up resources
db.close() #close the connection to the database to free up resources