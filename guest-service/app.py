from flask import Flask, jsonify, request

app = Flask(__name__)

guests = []

@app.route('/guests/book', methods=['POST'])
def book_guest_room():
    guest_id = request.json.get('guest_id')
    room_id = request.json.get('room_id')
    
    for guest in guests:
        if guest['guest_id'] == guest_id:
            guest.setdefault('booked_rooms', []).append(room_id)
            return jsonify({"message": f"Room {room_id} booked for guest {guest_id}!"}), 200
    return jsonify({"message": "Guest not found."}), 404

@app.route('/guests/<int:guest_id>', methods=['PUT'])
def update_guest(guest_id):
    updated_guest = request.json
    for guest in guests:
        if guest['guest_id'] == guest_id:
            guest.update(updated_guest)
            return jsonify(guest), 200
    return jsonify({"message": "Guest not found."}), 404

@app.route('/guests/<int:guest_id>', methods=['DELETE'])
def delete_guest(guest_id):
    global guests
    guests = [guest for guest in guests if guest['guest_id'] != guest_id]
    return jsonify({"message": "Guest deleted successfully."}), 200

@app.route('/guests', methods=['GET']) 
def get_guests():
    return jsonify(guests)

@app.route('/guests', methods=['POST'])
def add_guest():
    guest = request.json
    guests.append(guest)
    return jsonify(guest), 201

if __name__ == '__main__':
    app.run(port=5001)
