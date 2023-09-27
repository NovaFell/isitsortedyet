import sqlite3
from sqlite3 import Error
from time import sleep
from datetime import datetime

arr = [4, 3, 5, 2, 6, 8, 7, 9, 1]

def create_connection(db_file):
    try:
        return sqlite3.connect(db_file)
    except Error as e:
        print(e)
        return None

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

def check_for_array(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM array_data")
        result = cursor.fetchone()
        return result
    except Error as e:
        print(e)
        return None

def main():
    database = r".\\backend\\array.db"

    # create a database connection or get
    conn = create_connection(database)
    if not conn:
        print("Error connecting to the database")
        return

    try:
        # check if previous saved spot exists
        MEM_ARR = None
        created_at = None
        db_arr = check_for_array(conn)
        if not db_arr:
            # array does not exist in db create new initial save spot
            created_at = datetime.now()
            array_id = create_array(conn, created_at.strftime('%Y-%m-%d %H:%M:%S'), arr)
            if array_id:
                print(f"Array inserted at {created_at} with value: {arr}")
                MEM_ARR = arr
            else:
                print("Error inserting array")
                raise
        else:
            # get last saved list from db
            MEM_ARR = db_arr[2].split(',')
            created_at = datetime.strptime(db_arr[1], '%Y-%m-%d %H:%M:%S')

        while True:
            # array exists
            if ','.join(MEM_ARR) != db_arr[2]:
                print("BIT FLIP HAPPENED!!")
                # bit flip happened, save progress
                created_at = datetime.now()
                array_id = create_array(conn, created_at.strftime('%Y-%m-%d %H:%M:%S'), MEM_ARR)
                if array_id:
                    print("progress saved")
                else:
                    print("Error inserting array")
                    raise
            else:
                print(str(datetime.now()) + " - Array with the same elements, no bitflip yet. time since flip:" + str(datetime.now() - created_at))

            sleep(10)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
