from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

# URL to the guests and rooms services
guests_url = os.getenv("GUESTS_URL", "http://guests:5000")
rooms_url = os.getenv("ROOMS_URL", "http://rooms:5000")

@app.route('/status')
def status():
    # Check the status of the guests and rooms services
    guests_response = requests.get(f"{guests_url}/guests")
    rooms_response = requests.get(f"{rooms_url}/rooms")
    
    if guests_response.status_code == 200 and rooms_response.status_code == 200:
        return jsonify({"status": "all services are running"})
    else:
        return jsonify({"status": "some services are down"}), 500

@app.route('/guests')
def get_guests():
    response = requests.get(f"{guests_url}/guests")
    return response.json()

@app.route('/rooms')
def get_rooms():
    response = requests.get(f"{rooms_url}/rooms")
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
