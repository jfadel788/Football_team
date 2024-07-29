import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_mysql():
    connection = None  
    try:
        
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
            port=os.getenv('MYSQL_PORT')
        )

        if connection.is_connected():
            print("Connected to MySQL Server version ", connection.get_server_info())
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)

    return connection
def main():
    connect_to_mysql()
if __name__=="__main__":
    main()