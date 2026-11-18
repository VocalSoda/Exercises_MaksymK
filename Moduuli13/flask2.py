from flask import Flask, request
app = Flask(__name__)
import os
from dotenv import load_dotenv
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


def fetch_info(USER_ICAO):
    sql = f"SELECT * FROM airport WHERE ident = '{USER_ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    return result  



@app.route('/airport/<icao>') 
def get_info(icao):
    
    result = fetch_info(icao)
        
    if result:
        row = result[0]
        return f"airport ICAO : {icao}   airport name: {row[3]} and it is located in {row[10]} {row[8]}"
       
    else:
        return f"Airport with ICAO '{icao}' not found.", 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)