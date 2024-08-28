from flask import Flask, request, Response
import mysql.connector
import json

app = Flask(__name__)

@app.route('/airports/<icao>')
def get_airport_by_icao(icao: str = ...):
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        database = "airports", # created in a previous module
        collation = "utf8mb4_unicode_ci"
    )
    
    cursor = db.cursor(dictionary=True)
    sql_query = f"SELECT ident, name, municipality FROM airport WHERE ident = '{icao.upper()}'"
    
    try:
        cursor.execute(sql_query)
        data = cursor.fetchone()
        
        return data
    except Exception as error:
        return {"error": error}
    
# 404 handler
@app.errorhandler(404)
def page_not_found(status_code):
    response = {
        "status": 404,
        "message": "Invalid endpoint"
    }
    
    return Response(response=json.dumps(response), status=404, mimetype="application/json")

app.run(use_reloader=True, host="localhost", port=3000)