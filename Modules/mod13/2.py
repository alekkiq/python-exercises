from flask import Flask, request, Response
import mysql.connector

app = Flask(__name__)

@app.route('/airports/<icao>')
def get_airport_by_icao(icao: str):
    try: 
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password",
            database = "flight_game",
            collation = "utf8mb4_unicode_ci"
        )
        
        cursor = db.cursor(dictionary=True)
        sql_query = "SELECT ident, name, municipality FROM airport WHERE ident=%s"
        
        cursor.execute(sql_query, (icao,))
        data = cursor.fetchone()
        
        return data if data else {"message": "No data found"}
    except Exception as error:
        return error
    
# 404 handler
@app.errorhandler(404)
def page_not_found(status_code):
    response = {
        "status": 404,
        "message": "Invalid endpoint"
    }
    
    return response

app.run(use_reloader=True, host="localhost", port=3000)