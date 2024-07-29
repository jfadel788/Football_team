import mysql.connector
from database.connect import connect_to_mysql
from mysql.connector import Error
import mysql.connector
from dotenv import load_dotenv
def execute_querry(querry,params=None):
    connection=None
    try:
        connection=connect_to_mysql()
        if connection.is_connected():
            cursor=connection.cursor()
            if params:
                cursor.execute(querry,params)
            else :
                cursor.execute(querry)
        connection.commit()
        print("Querry executed sucessfully")
    except Error as e:
        print("Error while executing query", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
def create_player_table():
    query = """
    CREATE TABLE IF NOT EXISTS Player (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(200) NOT NULL,
        APT INT,
        SETT INT,
        AVG INT,
        Position VARCHAR(200),
        National_association VARCHAR(255)
    )
    """
    execute_querry(query)
    
def insert_player(first_name, last_name, apt, set_, avg, position, national_association):
    query = "INSERT INTO Player (first_name, last_name, APT, SETT, AVG, Position, National_association) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    params = (first_name, last_name, apt, set_, avg, position, national_association)
    execute_querry(query, params)

def update_player(id, first_name=None, last_name=None, apt=None, set_=None, avg=None, position=None, national_association=None):
    updates = []
    params = []
    
    if first_name is not None:
        updates.append("first_name = %s")
        params.append(first_name)
    if last_name is not None:
        updates.append("last_name = %s")
        params.append(last_name)
    if apt is not None:
        updates.append("APT = %s")
        params.append(apt)
    if set_ is not None:
        updates.append("`SET` = %s")
        params.append(set_)
    if avg is not None:
        updates.append("AVG = %s")
        params.append(avg)
    if position is not None:
        updates.append("Position = %s")
        params.append(position)
    if national_association is not None:
        updates.append("National_association = %s")
        params.append(national_association)
    params.append(id)
    set_clause = ", ".join(updates)
    query = f"UPDATE Player SET {set_clause} WHERE id = %s"
    
    execute_querry(query, tuple(params))

def main():
   update_player(1, first_name="Bob", last_name="Johnson", apt=15)
if __name__=="__main__":
    main()