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

def insert_teacher(connection, teacher):  # se pragmatiko project to teacher tha to pernousa san object TODO na psaksw ti ennououme me auto
    #tha borousa na balw kai ,table_name kai na ta pernaw me f string mesa sto cursor execute parakatw
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO teachers (id, firstname, lastname, age) VALUES (%s, %s, %s, %s)",
            teacher
        )
        connection.commit()
        print("Teacher inserted!")
    except Error as e:
        print(f"Error {e} occured")
        connection.rollback()
    finally:
        cursor.close()

def main():
    conn = create_connection('localhost', 'root', 'root', 'coding2025', '3306')
    teacher = (2, "Bob", "M.", 45)
    insert_teacher(conn, teacher)
    conn.close()
    print("Connection closed")

if __name__ == "__main__":
    main()
