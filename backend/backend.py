import sqlite3
from sqlite3 import Error
import datetime

arr = [4, 3, 5, 2, 6, 8, 7, 9, 1]

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS array_data (
                id INTEGER PRIMARY KEY,
                created_at TEXT NOT NULL,
                elements TEXT NOT NULL
            )
        """)
        conn.commit()
    except Error as e:
        print(e)

def create_array(conn, created_at, elements):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO array_data (created_at, elements) VALUES (?, ?)",
                       (created_at, ",".join(map(str, elements))))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def check_for_array(conn, elements):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM array_data WHERE elements = ?",
                       (",".join(map(str, elements)),))
        result = cursor.fetchone()
        return result is not None
    except Error as e:
        print(e)
        return False

def main():
    database = r".\\backend\\array.db"

    while True:
        # create a database connection
        conn = create_connection(database)
        if conn is not None:
            create_table(conn)  # Create the table if it doesn't exist
            
            # Check if the array already exists in the database
            if check_for_array(conn, arr):
                print("Array with the same elements already exists in the database.")
            else:
                created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                array_id = create_array(conn, created_at, arr)
                if array_id:
                    print(f"Array inserted with ID: {array_id}")
                else:
                    print("Error inserting array")
            conn.close()
        else:
            print("Error connecting to the database")

if __name__ == '__main__':
    main()
