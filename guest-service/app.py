from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

# Store guests
guests = []

# URL to the rooms service
rooms_url = os.getenv("ROOMS_URL", "http://rooms:5000")

@app.route('/guests', methods=['GET'])
def get_guests():
    return jsonify(guests)

@app.route('/guests', methods=['POST'])
def add_guest():
    data = request.json
    room_id = data.get("room_id")
    guest_name = data.get("guest_name")

    # Check if the room exists and is available
    room_response = requests.get(f"{rooms_url}/rooms/{room_id}")
    if room_response.status_code == 200:
        room = room_response.json()
        if room["available"]:
            guest = {"guest_name": guest_name, "room_id": room_id}
            guests.append(guest)
            return jsonify(guest), 201
        else:
            return jsonify({"error": "Room is not available"}), 400
    else:
        return jsonify({"error": "Room not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
