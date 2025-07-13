import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name, port):
    connection = None

    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name,
            port = port
        )
        print("Connection to MySQL DB successfull")
    except Error as e:
        print(f"Error {e} occured")
    return connection

def create_tables(connection):
    create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50)
    )
    """
    create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50),
        age INTEGER
    )
    """
    cursor = connection.cursor()

    try:
        cursor.execute('BEGIN')
        cursor.execute(create_teachers_table)
        cursor.execute(create_students_table)
        connection.commit()
    except Error as e:
        print(f"Error {e} occured")
        connection.rollback()
    finally:
        cursor.close()

def main():
    conn = create_connection('localhost', 'root', 'root', 'coding2025', '3306')

    if conn:
        create_tables(connection=conn)
        conn.close()
        print("MySQL Connection is closed")

if __name__ == "__main__":
    main()
