import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None

    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )

        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"Error: {e} occured")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"Error: {e} occured")
    finally:
        cursor.close()

def main():
    conn = create_connection('localhost', 'root', 'root')  # Edw xreiazomai ta admin credentials oxi kapoiou user!!!!

    if conn:
        create_db_query = "CREATE DATABASE coding2025"
        create_database(conn, create_db_query)
        conn.close()
        print("MySQL connection is closed.")

if __name__ == "__main__":
    main()