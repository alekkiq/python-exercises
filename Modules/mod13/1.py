from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/prime_number/<number>')
def prime_number(number: int | str = 1) -> dict:
    number = int(number)

    # src: stackoverflow
    is_prime = number > 1 and all(number % i for i in range(2, int(number ** 0.5) + 1))

    return {"number": number, "isPrime": is_prime}

# 404 handler
@app.errorhandler(404)
def page_not_found(status_code):
    response = {
        "status": 404,
        "message": "Invalid endpoint"
    }
    
    return Response(response=json.dumps(response), status=404, mimetype="application/json")

app.run(use_reloader=True, host="localhost", port=3000)