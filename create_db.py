import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('eosmedspa.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table called 'clients' with the specified columns
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        date_added DATE,
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        email_address TEXT,
        phone_number TEXT,
        street_address_1 TEXT,
        street_address_2 TEXT,
        city TEXT,
        state TEXT,
        zip_code TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and 'clients' table created successfully.")
