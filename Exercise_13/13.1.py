from flask import Flask, Response
import json

# Creating App route
app = Flask(__name__)
@app.route('/check/<number>')


def prime_num(number): # Prime number Function
    number = int(number)
    for x in range(2, number):
        if number % x == 0:
            response = {
                "Number": number,
                "Prime": "No"
            }
            return response

    else:
        response = {
            "Number": number,
            "Prime": "Yes"
        }
    return response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint - Add '/check/<number>' to URL to get result",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

# Launching Backend program to browser
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=1234)