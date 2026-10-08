# it_inventory

Project for CS100.

This project is a Python program that connects to MySQL running on a locally hosted virtual machine (VM). It helps keep device information, including IP addresses and device details, organized in a database.

## What the program does

The program uses a command-line menu to manage device records:

1. **Add Device** — enter a device's ID, name, type, IP address, and location to save it in the database.
2. **View Devices** — display the devices stored in the database.
3. **Update Device** — change a device's information using its ID.
4. **Delete Device** — remove a device using its ID.
5. **Exit** — leave the program.

## Device information

The MySQL database is named `it_inventory`. Device records are stored in the `devices` table.

| Field | Information stored |
| --- | --- |
| `id` | Device ID |
| `name` | Device name |
| `device_type` | Type of device, such as a laptop, desktop, or server |
| `ip_address` | Device IP address |
| `location` | Device location |

## How the code works

The program imports `mysql.connector` to connect Python to MySQL.

- `show_menu()` displays the menu options.
- `add_device(cursor, db)` collects device information and uses an SQL `INSERT` statement to save it.
- `view_devices(cursor)` uses an SQL `SELECT` statement to retrieve and display device records.
- `update_device` uses an SQL `UPDATE` statement to change a record by ID.
- `delete_device` uses an SQL `DELETE` statement to remove a record by ID and checks whether a record was deleted.

The menu repeats so the user can perform multiple actions. SQL statements use `%s` placeholders to pass entered values separately from the SQL text.

## Database connection

The current connection settings use:

| Setting | Value |
| --- | --- |
| Host | `127.0.0.1` |
| Port | `3306` |
| User | `inventory_app` |
| Database | `it_inventory` |

The program also supplies the database user's password when connecting. The Python environment needs `mysql.connector`, and the MySQL database and `devices` table need to exist before the program can use them.

## Setup and progress screenshots

### Checking whether MySQL is running

<img width="830" height="341" alt="Checking whether MySQL is running" src="https://github.com/user-attachments/assets/5c341b2a-bd08-43fe-938d-61242aa4deaa" />

### Additional setup and project progress

These screenshots document the setup and work completed on the project.

<img width="704" height="222" alt="Project setup screenshot 1" src="https://github.com/user-attachments/assets/4b22bebf-e155-45ec-9af2-5bd5417e9133" />

<img width="320" height="295" alt="Project setup screenshot 2" src="https://github.com/user-attachments/assets/09283206-6256-41fe-8d16-c08523dcb5fb" />

<img width="341" height="154" alt="Project setup screenshot 3" src="https://github.com/user-attachments/assets/c15d0613-15a8-4560-aec5-89de38497e42" />

<img width="568" height="200" alt="Project setup screenshot 4" src="https://github.com/user-attachments/assets/a04002c5-a27b-4e70-bd94-9baa0e252fe3" />

<img width="572" height="104" alt="Project setup screenshot 5" src="https://github.com/user-attachments/assets/fd51efbf-5378-4ebe-a3e5-5190e9c0cd30" />

<img width="574" height="209" alt="Project setup screenshot 6" src="https://github.com/user-attachments/assets/ffefe0df-bd96-461a-ae08-f006b854f7f2" />

<img width="914" height="794" alt="Project progress screenshot 7" src="https://github.com/user-attachments/assets/65d334f0-36f9-438d-8666-69acc700133a" />

<img width="762" height="75" alt="Project progress screenshot 8" src="https://github.com/user-attachments/assets/8458aac9-654d-4430-8c63-69f23cada2dc" />

<img width="589" height="188" alt="Project progress screenshot 9" src="https://github.com/user-attachments/assets/21a8f66e-d33c-4575-b3c3-136476a0e959" />

### Changing the MySQL bind address

During setup, I used `nano` to edit the MySQL configuration file. I changed `bind-address` to `0.0.0.0` and left the MySQL X Protocol bind address (`mysqlx-bind-address`) at the loopback address.

<img width="1201" height="717" alt="MySQL bind-address configuration" src="https://github.com/user-attachments/assets/fa74eae5-f437-432e-bb46-84f6acedef32" />
