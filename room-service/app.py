from flask import Flask, jsonify, request

app = Flask(__name__)

rooms = [
    {"room_id": 1, "room_name": "Single Room", "available": True},
    {"room_id": 2, "room_name": "Double Room", "available": True},
    {"room_id": 3, "room_name": "Suite", "available": False}
]

@app.route('/rooms/book', methods=['POST'])
def book_room():
    room_id = request.json.get('room_id')
    for room in rooms:
        if room['room_id'] == room_id:
            if room['available']:
                room['available'] = False
                return jsonify({"message": f"Room {room['room_name']} booked successfully!"}), 200
            else:
                return jsonify({"message": "Room is not available."}), 400
    return jsonify({"message": "Room not found."}), 404

@app.route('/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    updated_room = request.json
    for room in rooms:
        if room['room_id'] == room_id:
            room.update(updated_room)
            return jsonify(room), 200
    return jsonify({"message": "Room not found."}), 404

@app.route('/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    global rooms
    rooms = [room for room in rooms if room['room_id'] != room_id]
    return jsonify({"message": "Room deleted successfully."}), 200

@app.route('/rooms', methods=['GET'])
def get_rooms():
    return jsonify(rooms)

@app.route('/rooms', methods=['POST'])
def add_room():
    room = request.json
    rooms.append(room)
    return jsonify(room), 201

if __name__ == '__main__':
    app.run(port=5002)
