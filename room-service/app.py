from flask import Flask, jsonify

app = Flask(__name__)

# Sample rooms
rooms = [
    {"room_id": 1, "room_name": "Single Room", "available": True},
    {"room_id": 2, "room_name": "Double Room", "available": True},
    {"room_id": 3, "room_name": "Suite", "available": False}
]

@app.route('/rooms')
def get_rooms():
    return jsonify(rooms)

@app.route('/rooms/<int:room_id>')
def get_room(room_id):
    room = next((r for r in rooms if r["room_id"] == room_id), None)
    if room:
        return jsonify(room)
    else:
        return jsonify({"error": "Room not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
