import random
from flask import Flask, jsonify

app = Flask(__name__)

def get_spo2():
    """Simulates a random SpO2 value (replace with real data from band in production)"""
    return random.randint(90, 99)  # Simulates values between 90% and 99%

@app.route('/get_spo2')
def get_spo2_data():
    """Returns simulated SpO2 data as a JSON response"""
    spo2_value = get_spo2()
    response = {
        "spo2_level": spo2_value
    }
    return jsonify(response), 200  # Return JSON data with status code 200 (OK)

if __name__ == '__main__':
    app.run(debug=True)  # Enable debugging for development
