from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Room Service URL
ROOM_SERVICE_URL = 'http://rooms:5002'
# Guest Service URL
GUEST_SERVICE_URL = 'http://guests:5001'

# Room Service Endpoints
@app.route('/rooms', methods=['GET'])
def get_rooms():
    response = requests.get(f"{ROOM_SERVICE_URL}/rooms")
    return jsonify(response.json()), response.status_code

@app.route('/rooms/book', methods=['POST'])
def book_room():
    room_id = request.json.get('room_id')
    response = requests.post(f"{ROOM_SERVICE_URL}/rooms/book", json={"room_id": room_id})
    return jsonify(response.json()), response.status_code

# Guest Service Endpoints
@app.route('/guests', methods=['GET'])
def get_guests():
    response = requests.get(f"{GUEST_SERVICE_URL}/guests")
    return jsonify(response.json()), response.status_code

@app.route('/guests/book', methods=['POST'])
def book_guest_room():
    guest_id = request.json.get('guest_id')
    room_id = request.json.get('room_id')
    response = requests.post(f"{GUEST_SERVICE_URL}/guests/book", json={"guest_id": guest_id, "room_id": room_id})
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=5000)
