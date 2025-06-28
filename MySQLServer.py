import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

try:
    my_db = mysql.connector.connect(
        host = os.environ["DB_HOST"],
        user = os.environ["DB_USE"],
        password = os.environ["DB_PASSWORD"],
        database = os.environ["DB"]
    )
except Exception as e:
    print(f"Error: {e}")
except mysql.connector.Error as e:
    print(f"Error: {e}")
else:
    print("Connected successfully!")

my_cursor = my_db.cursor()

my_cursor.execute('''CREATE DATABASE IF NOT EXISTS alx_book_store''')

my_cursor.close()
my_db.close()