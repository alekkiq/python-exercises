from flask import Flask
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "flight_game",
    collation = "utf8mb4_unicode_ci"
)

@app.route("/airports/<icao>")
def get_airport_by_icao(icao: str):
    try: 
        cursor = db.cursor(dictionary=True)
        sql_query = "SELECT ident, name, municipality FROM airport WHERE ident=%s"
        
        cursor.execute(sql_query, (icao,))
        data = cursor.fetchone()
        
        if not data:
            raise Exception("Airport not found")
        
        return data
    except Exception as error:
        return {"error": str(error)}, 404
    
# 404 handler
@app.errorhandler(404)
def page_not_found(message):
    return {
        "status": 404,
        "message": "Invalid endpoint"
    }, 404

app.run(use_reloader=True, host="localhost", port=3000)