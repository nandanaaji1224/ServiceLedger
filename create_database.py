import sqlite3

# Define the database file name
DATABASE_FILE = 'salon_data.db'

def create_transactions_table():
    """Connects to the SQLite database and creates the transactions table if it doesn't exist with updated date and time formats."""
    try:
        # Establish a connection to the database
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # SQL command to create the transactions table with updated date and time formats
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_date TEXT NOT NULL,
            transaction_time TEXT NOT NULL,
            customer_name TEXT,
            phone_number TEXT,
            service TEXT NOT NULL,
            service_cost REAL NOT NULL,
            payment_mode TEXT NOT NULL,
            transaction_type TEXT NOT NULL
        );
        """

        # Execute the SQL command
        cursor.execute(create_table_sql)

        # Commit the changes
        conn.commit()
        print(f"Table 'transactions' created (or already existed) in '{DATABASE_FILE}'")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the database connection
        if conn:
            conn.close()

if __name__ == "__main__":
    create_transactions_table()
