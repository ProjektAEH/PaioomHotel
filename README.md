# Hotel Management App

## Overview
This is a hotel management application with microservices for managing guests and rooms.

## Services
- **Guest Service**: Manages guest information.
- **Room Service**: Manages room information.

## Running the Services
1. Navigate to the `guest-service` directory and install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the guest service:
   ```
   python app.py
   ```

3. Navigate to the `room-service` directory and install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the room service:
   ```
   python app.py
   ```

## API Endpoints
### Guest Service
- `GET /guests`: Retrieve the list of guests.
- `POST /guests`: Add a new guest.

### Room Service
- `GET /rooms`: Retrieve the list of rooms.
- `POST /rooms`: Add a new room.
