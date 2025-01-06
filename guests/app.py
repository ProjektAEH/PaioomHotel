from flask import Flask, jsonify, request
import os
import requests
from database import create_table, add_guest, get_all_guests

app = Flask(__name__)

# URL do mikroserwisu rooms
rooms_url = os.getenv("ROOMS_URL", "http://rooms:5000")

# Inicjalizacja bazy danych
create_table()

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = get_all_guests()
    return jsonify(guests)

@app.route('/guests', methods=['POST'])
def add_guest_to_room():
    data = request.json
    room_id = data.get("room_id")
    guest_name = data.get("guest_name")

    # Sprawdź, czy pokój istnieje i jest dostępny
    room_response = requests.get(f"{rooms_url}/rooms/{room_id}")
    if room_response.status_code == 200:
        room = room_response.json()
        if room["available"]:
            # Dodaj gościa do bazy danych
            add_guest(guest_name, room_id)

            # Zaktualizuj dostępność pokoju
            room["available"] = False  # Pokój teraz jest zajęty
            requests.put(f"{rooms_url}/rooms/{room_id}", json=room)

            return jsonify({"guest_name": guest_name, "room_id": room_id}), 201
        else:
            return jsonify({"error": "Room is not available"}), 400
    else:
        return jsonify({"error": "Room not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
