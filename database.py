import sqlite3
import os
from sqlite3 import Error

# Ścieżka do pliku bazy danych
DATABASE = os.path.join(os.path.dirname(__file__), 'guests.db')

# Funkcja do połączenia z bazą danych
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except Error as e:
        print(e)
    return conn

# Funkcja do tworzenia tabeli gości
def create_table():
    conn = create_connection()
    if conn:
        try:
            sql_create_guests_table = """
            CREATE TABLE IF NOT EXISTS guests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guest_name TEXT NOT NULL,
                room_id INTEGER NOT NULL
            );
            """
            conn.execute(sql_create_guests_table)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

# Funkcja do dodawania gościa do bazy danych
def add_guest(guest_name, room_id):
    conn = create_connection()
    if conn:
        try:
            sql = 'INSERT INTO guests (guest_name, room_id) VALUES (?, ?)'
            conn.execute(sql, (guest_name, room_id))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

# Funkcja do pobierania wszystkich gości
def get_all_guests():
    conn = create_connection()
    guests = []
    if conn:
        try:
            sql = 'SELECT guest_name, room_id FROM guests'
            cursor = conn.execute(sql)
            guests = cursor.fetchall()
        except Error as e:
            print(e)
        finally:
            conn.close()
    return guests
