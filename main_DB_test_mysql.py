import mysql.connector #this is the library that allows us to connect to MySQL databases

BLUE = "\033[94m"
RESET = "\033[0m"

print(BLUE + """
██████╗ ██╗██╗   ██╗███████╗██████╗
██╔══██╗██║██║   ██║██╔════╝██╔══██╗
██████╔╝██║██║   ██║█████╗  ██████╔╝
██╔══██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║  ██║██║ ╚████╔╝ ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
""" + RESET)
print()
# The fields in the table devices are as follows:
# - id: an integer that is the primary key for the table
# - name: a string that is the name of the device
# - device_type: a string that is the type of device (e.g. laptop, desktop, server, etc.)
# - ip_address: a string that is the IP address of the device
# - location: a string that is the location of the device

def show_menu():
    print()
    print('===== IT Inventory Management System =====')
    print()
    print('1. Add Device')
    print('2. View Devices')
    print('3. Update Device')
    print('4. Delete Device')
    print('5. Exit')
    print()

def add_device(cursor, db):
    id = input("Enter the number/id of the device: ")
    name = input("Enter device name: ")
    device_type = input("Enter device type: ")
    ip_address = input("Enter device IP address: ")
    location = input("Enter device location: ")
    
    sql = """
    INSERT INTO devices (id, name, device_type, ip_address, location)
    VALUES (%s, %s, %s, %s, %s) 
    """ # the %s 
    values = (id, name, device_type, ip_address, location)

    cursor.execute(sql, values)

    db.commit() #commit the changes to the database

    print('Device added successfully!') #print a message to the console to confirm that the device was added successfully

def view_devices(cursor):
    cursor.execute('select * from devices')
    results = cursor.fetchall()

    for device in results:
        id, name, device_type, ip_address, location = device

        print()
        print(f"ID: {id}")
        print(f"Name: {name}")
        print(f"Type: {device_type}")
        print(f"IP Address: {ip_address}")
        print(f"Location: {location}")

def update_device(cursor, db):
    id = input('Enter the ID of the device you want to update: ')
    name = input("Enter new device name: ")
    device_type = input("Enter new device type: ")
    ip_address = input("Enter new device IP address: ")
    location = input("Enter new device location: ") 
    sql = '''
    UPDATE devices
    set name = %s,
        device_type = %s,
        ip_address = %s,
        location = %s
    WHERE id = %s
    '''
    values = (name, device_type, ip_address, location, id)
    cursor.execute(sql, values)
    db.commit()

    print('Device updated successfully!')

def delete_device(cursor, db):
    id = input('Enter the ID of the device you want to delete: ')

    sql = '''
    DELETE FROM devices
    WHERE id = %s
    '''

    values = (id,)

    cursor.execute(sql, values)
    db.commit()

    if cursor.rowcount > 0:
        print(f'Item ID: {id} was successfully deleted.')
    else:
        print(f'No device with ID {id} was found.')

db = mysql.connector.connect(   #checking to see if we can connect to the database 
    host="127.0.0.1",   #the db variable is now a connection object that we can use to interact with the database
    user="inventory_app",
    port = 3306,
    password="mhriver",
    database="it_inventory"
)

cursor = db.cursor() #create a cursor object that we can use to execute SQL queries

print("Connected to MySQL!") #print a message to the console to confirm the connection



while True:
    show_menu() #call the show_menu function to display the menu options to the user

    choice = input("Enter your choice (1/2/3/4/5): ") #prompt the user to enter their choice

    if choice == "1":
        print('Add Device Selected')
        print()
        add_device(cursor, db)
    elif choice == "2":
        print('View Device selected')
        print()
        view_devices(cursor)
    elif choice == "3":
        print('Update selected')
        print()
        update_device(cursor, db)
    elif choice == '4':
        print('Delete item selected')
        print()
        delete_device(cursor, db)
    elif choice == '5':
        print('Exiting...')
        break
    else:
        print('Invalid choice. Please try again.')


cursor.close() #close the cursor object to free up resources
db.close() #close the connection to the database to free up resources