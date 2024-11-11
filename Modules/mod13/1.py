from flask import Flask

app = Flask(__name__)

@app.route('/prime-number/<number>')
def prime_number(number: int | str = 1):
    try:
        number = int(number)

        is_prime = number > 1 and all(number % i for i in range(2, int(number ** 0.5) + 1))

        return {"number": number, "isPrime": is_prime}, 200
    except ValueError:
        return {"error": "Invalid number"}, 400

# 404 handler
@app.errorhandler(404)
def not_found(status_code):
    return {
        "status": 404,
        "message": "Invalid endpoint"
    }, 404

app.run(use_reloader=True, host="localhost", port=3000)