import sqlite3
from datetime import datetime

def add_new_client():
    # Connect to the SQLite database
    conn = sqlite3.connect('eosmedspa.db')
    cursor = conn.cursor()

    # Get current date
    date_added = datetime.now().strftime('%Y-%m-%d')

    # Prompt the user to enter information for the new client
    first_name = input("Enter the first name: ")
    middle_name = input("Enter the middle name: ")
    last_name = input("Enter the last name: ")
    email_address = input("Enter the email address: ")
    phone_number = input("Enter the mobile phone number: ")
    street_address_1 = input("Enter the address (Line 1): ")
    street_address_2 = input("Enter the address (Line 2): ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    zip_code = input("Enter the zip code: ")

    # Insert the new client record into the 'clients' table
    cursor.execute('''
        INSERT INTO clients (
            date_added, first_name, middle_name, last_name, email_address,
            phone_number, street_address_1, street_address_2, city, state, zip_code
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        date_added, first_name, middle_name, last_name, email_address,
        phone_number, street_address_1, street_address_2, city, state, zip_code
    ))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"New client '{first_name} {last_name}' added successfully.")

# Example usage
add_new_client()
