import os
from dotenv import load_dotenv, dotenv_values
import mysql.connector
load_dotenv()

connection = mysql.connector.connect(
    host = os.getenv("HOST"),
    port = os.getenv("PORT"),
    database = os.getenv("DATABASE"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    autocommit = True
)


